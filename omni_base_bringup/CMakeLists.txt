cmake_minimum_required(VERSION 3.8)
project(omni_base_bringup)

find_package(ament_cmake_auto REQUIRED)

# PAL Robotics stricter build flags, other developers should not worry about this
find_package(ament_cmake_pal QUIET)

ament_auto_find_build_dependencies()

if(pal_module_cmake_FOUND)
  pal_register_modules(
    module/twist_mux.yaml
    module/joystick.yaml
  )
endif()

ament_auto_package(INSTALL_TO_SHARE config launch)
