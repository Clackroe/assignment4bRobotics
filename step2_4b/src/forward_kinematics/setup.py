from setuptools import find_packages, setup

package_name = 'a4_ac'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='sayantan',
    maintainer_email='sdatta3@uncc.edu',
    description='Assignment 4 ITCS 4151 Spring 2024',
    license='CC BY-SA 4.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'joint_state_tf_ac = forward_kinematics.a4_ac:main'
        ],
    },
)
