#!/usr/bin/env python3

# Xander Cole 
# acole67@uncc.edu

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState

from tf2_ros import TransformBroadcaster
import math
import numpy as np

from geometry_msgs.msg import TransformStamped
from scipy.spatial.transform import Rotation as R
from tf_transformations import quaternion_from_euler

def convertMatToTf_scipy(mat):
    ''' Convert transformation matrix to TransformStamped message
    '''
    result = TransformStamped()
    # Translation is set based on position vector in transformation matrix
    result.transform.translation.x = mat[0,3]
    result.transform.translation.y = mat[1,3]
    result.transform.translation.z = mat[2,3]
    rot_mat = mat[0:3,0:3]
    r = R.from_matrix(rot_mat)
    q = r.as_quat()
    # Set rotation
    result.transform.rotation.x = q[0]
    result.transform.rotation.y = q[1]
    result.transform.rotation.z = q[2]
    result.transform.rotation.w = q[3]
    return result

def getT(theta_i, a_iMinusOne, alpha_iMinusOne, d_i):
    ''' Create the transformation matrix from DH parameters
    Args:
        theta_i: float, angle in radians
        a_iMinusOne: float, length of the common normal
        alpha_iMinusOne: float, angle in radians
        d_i: float, link offset
    Returns:
        result: np.array, transformation matrix
    '''
    result = np.zeros((4,4))
    # TODO: fill in the transformation matrix
    return result

def dh_parameters_to_mat(dh_params):
    ''' Create the transformation matrix from DH parameters
    '''
    Ts = [] # list of transformation matrices
    T_40 = np.eye(4) # identity matrix
    # TODO: loop through all the dh parameters and create the transformation matrices
    # HINT: Remember to multiply the transformation matrices
    # HINT: Use the getT function to get the transformation matrix
    # HINT: Use the @ operator to multiply the transformation matrices
    # HINT: Use the np.round function to round the transformation matrices before printing to avoid a lot of floating point numbers
    return T_40


class JointStateSubscriber(Node):
    def __init__(self):
        super().__init__('joint_state_subscriber')
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_state_callback,
            10
        )
        self.subscription
        # -- initialize a publisher for TF
        self.tf_broadcaster = TransformBroadcaster(self)

        # -- initialize the link lengths
        self.l1 = l1 = 3.0
        self.l2 = l2 = 3.0
        self.l3 = l3 = 2.0

        # -- TODO: initialize the dh parameters
        # HINT: Do not initialize joint angle thetas here
        # HINT: Initialize the joint angle thetas in the callback function
        # self.dh_params = dh_params = {}
        # dh_params['joints'] = # List of joint names
        # dh_params['d'] = # List of 'd' values for each joint[l1, 0.0, 0.0, 0.0, 0.0]
        # dh_params['alpha'] = # List of alpha angles0]
        # dh_params['a'] = # List of 'a' or link length values 
        # dh_params['theta'] = # Theta angles initialize to zeros

        #list of dicts
        self.dh_params = dh_params = {}
        dh_params['joints'] = ['0', '1', '2', '3']
        dh_params['d'] = [0, 0, 0, 0]
        dh_params['alpha'] = [0, 0, 90, 0]
        dh_params['a'] = [0, 0, 0, l2]
        dh_params['theta'] = [0, 0, 0, 0]

        t0_3 = self.dh_parameters_to_mat(dh_params)


    def joint_state_callback(self, msg):
        ''' Callback function for joint state subscriber
        '''
        # -- TODO: Get your joint state values for the 3R manipulator
        
        names = msg.name
        positions = msg.position


        # -- TODO: Set up thetas for DH parameters

        for i, n in enumerate(names):
            index = int(n)
            self.dh_params['theta'][index] = positions[i]
        

        # -- Create the transformation matrix
        T_BE = np.array([
            [],
            [],
            [].
            []
            ]) @ dh_parameters_to_mat(self.dh_params)


        
        # HINT: Printing the intermediate transformation matrices will help you debug
        # HINT: Printing the final transformation matrix will help you verify your solution

        # -- create transformation message from the matrix
        tf_msg = convertMatToTf_scipy(T_BE)
        tf_msg.header.frame_id = 'ac'
        tf_msg.child_frame_id = 'xander_cole' # TODO: Replace with your name
        # Send the transformation
        self.tf_broadcaster.sendTransform(tf_msg)

def main():
    rclpy.init()
    node = JointStateSubscriber()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    rclpy.shutdown()

