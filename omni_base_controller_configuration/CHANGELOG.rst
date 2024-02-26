^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package omni_base_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.0.4 (2024-02-26)
------------------
* Merge branch 'abr/fix/controller' into 'humble-devel'
  fix wheel_radius and wheel_separation
  See merge request robots/omni_base_robot!17
* fix wheel_radius and wheel_separation
* Contributors: antoniobrandi

2.0.3 (2024-02-02)
------------------

2.0.2 (2023-12-15)
------------------

2.0.1 (2023-12-11)
------------------
* Merge branch 'fix/modules-ros2' into 'humble-devel'
  fix modules
  See merge request robots/omni_base_robot!14
* moved omni modules from 00 to 10
* Contributors: Noel Jimenez, andreacapodacqua

2.0.0 (2023-11-22)
------------------
* Merge branch 'feat/module' into 'humble-devel'
  Feat/module
  See merge request robots/omni_base_robot!13
* fix deps
* fix default controllers
* using correct name
* split bringup module
* omni_base ROS 2
* add imu_sensor_broadcaster fix robot_model
* ROS 2 omni base robot
* Update mobile_base_controller to work with omni_drive_controller
* chore: wheel odometry calibration params recom
* disable controller and add TODO
* enable control(er) and 2dnav
* fix: Load gazebo_controller_manager_cfg.yaml and launch only omnibase stuff that is ready
* omnibase controller configuration to ROS 2:
  + yaml
  + launch.py
* omnibase controller conf to colcon
* Contributors: YueErro, andreacapodacqua, antoniobrandi, josecarlos

0.0.10 (2022-12-27)
-------------------

0.0.9 (2022-10-24)
------------------
* Merge branch 'feat/robust-odometry-integration' into 'ferrum-devel'
  disabled odom tf publication
  See merge request robots/omni_base_robot!6
* disabled odom tf publication
* Contributors: josegarcia

0.0.8 (2022-08-16)
------------------

0.0.7 (2022-08-10)
------------------
* Merge branch 'fix_base_collision' into 'ferrum-devel'
  Fix collision boxes for the base
  See merge request robots/omni_base_robot!3
* Remove extra joints because were changed to fixed
* Contributors: saikishor, thomaspeyrucain

0.0.6 (2022-06-17)
------------------

0.0.5 (2021-11-24)
------------------
* add new controller parameters for the integration with the new omni_drive_controller
* Contributors: antoniobrandi

0.0.4 (2021-11-04)
------------------

0.0.3 (2021-10-05)
------------------

0.0.2 (2021-09-30)
------------------

0.0.1 (2021-09-30)
------------------
* preparing release changed version
* preparing release
* Fixing wheel naming convention using rear instead of back
* Merge branch 'omni_base_sw' into 'master'
  Omni base sw
  See merge request robots/omni_base_robot!1
* fix the wheel frame names in the mobile base controller
* Changed laser scan topic for the simulation navigation
* on of the urdf and completed controller configuration
* Contributors: Sai Kishor Kothakota, antoniobrandi
