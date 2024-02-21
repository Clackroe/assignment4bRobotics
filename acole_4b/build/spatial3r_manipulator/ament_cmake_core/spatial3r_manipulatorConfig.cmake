# generated from ament/cmake/core/templates/nameConfig.cmake.in

# prevent multiple inclusion
if(_spatial3r_manipulator_CONFIG_INCLUDED)
  # ensure to keep the found flag the same
  if(NOT DEFINED spatial3r_manipulator_FOUND)
    # explicitly set it to FALSE, otherwise CMake will set it to TRUE
    set(spatial3r_manipulator_FOUND FALSE)
  elseif(NOT spatial3r_manipulator_FOUND)
    # use separate condition to avoid uninitialized variable warning
    set(spatial3r_manipulator_FOUND FALSE)
  endif()
  return()
endif()
set(_spatial3r_manipulator_CONFIG_INCLUDED TRUE)

# output package information
if(NOT spatial3r_manipulator_FIND_QUIETLY)
  message(STATUS "Found spatial3r_manipulator: 0.0.0 (${spatial3r_manipulator_DIR})")
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "Package 'spatial3r_manipulator' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  # optionally quiet the deprecation message
  if(NOT ${spatial3r_manipulator_DEPRECATED_QUIET})
    message(DEPRECATION "${_msg}")
  endif()
endif()

# flag package as ament-based to distinguish it after being find_package()-ed
set(spatial3r_manipulator_FOUND_AMENT_PACKAGE TRUE)

# include all config extra files
set(_extras "")
foreach(_extra ${_extras})
  include("${spatial3r_manipulator_DIR}/${_extra}")
endforeach()
