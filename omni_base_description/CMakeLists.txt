cmake_minimum_required(VERSION 3.8)
project(omni_base_description)

find_package(ament_cmake_auto REQUIRED)
find_package(ament_cmake_python REQUIRED)

# PAL Robotics stricter build flags, other developers should not worry about this
find_package(ament_cmake_pal QUIET)

ament_auto_find_build_dependencies()

if(pal_module_cmake_FOUND)
  pal_register_modules(
    module/00_robot_state_publisher.yaml
  )
endif()

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

ament_auto_package(INSTALL_TO_SHARE gazebo launch meshes robots ros2_control urdf config)
