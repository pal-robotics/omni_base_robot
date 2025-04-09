^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package omni_base_controller_configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.10.1 (2025-04-09)
-------------------

2.10.0 (2025-03-25)
-------------------

2.9.0 (2025-02-24)
------------------

2.8.0 (2025-01-23)
------------------

2.7.0 (2025-01-22)
------------------

2.6.0 (2025-01-16)
------------------

2.5.2 (2024-11-22)
------------------
* Merge branch 'abr/fix/twist-relay' into 'humble-devel'
  using execute process to respawn twist_relay node
  See merge request robots/omni_base_robot!53
* using execute process to respawn twist_relay node
* Contributors: antoniobrandi

2.5.1 (2024-11-08)
------------------

2.5.0 (2024-11-06)
------------------
* Set update_rate for joint_state_broadcaster
* Contributors: Noel Jimenez

2.4.2 (2024-10-18)
------------------

2.4.1 (2024-10-15)
------------------

2.4.0 (2024-09-04)
------------------
* Only relay cmd_vel topic in simulation
* Contributors: David ter Kuile

2.3.0 (2024-08-29)
------------------
* use relay for cmd_vel message
* Refactor mobile base controller
* Contributors: David ter Kuile

2.2.0 (2024-08-08)
------------------
* Use unlesscondition
* start mobile_base_controller only for real robot
* Contributors: David ter Kuile, antoniobrandi

2.1.0 (2024-08-07)
------------------
* Use controller_type from the controllers config
* Remove use_stamped_vel parameter
* Contributors: Noel Jimenez

2.0.19 (2024-07-09)
-------------------
* Add warning for pal_module_cmake not found
* Contributors: Noel Jimenez

2.0.18 (2024-07-01)
-------------------

2.0.17 (2024-06-28)
-------------------

2.0.16 (2024-06-26)
-------------------
* Merge branch 'dtk/move-robot-args' into 'humble-devel'
  Dtk/move robot args
  See merge request robots/omni_base_robot!34
* Change import for launch args
* Contributors: David ter Kuile, davidterkuile

2.0.15 (2024-06-25)
-------------------
* Merge branch 'tpe/upate_std_and_launch_arg' into 'humble-devel'
  Standardize urdf + update lauch args
  See merge request robots/omni_base_robot!32
* Restructure gazebo urdf
* Update linters
* Add public sim
* Fix base_controller type
* Update URDF structure
* Contributors: David ter Kuile, davidterkuile

2.0.14 (2024-06-13)
-------------------

2.0.13 (2024-06-03)
-------------------
* Merge branch 'abr/fix/min-acc' into 'humble-devel'
  added min acceleration parameters
  See merge request robots/omni_base_robot!31
* typo
* added min acceleration parameters
* Contributors: antoniobrandi

2.0.12 (2024-06-03)
-------------------

2.0.11 (2024-05-21)
-------------------

2.0.10 (2024-04-18)
-------------------

2.0.9 (2024-04-11)
------------------
* Merge branch 'dtk/fix/update-module-numbers' into 'humble-devel'
  Dtk/fix/update module numbers
  See merge request robots/omni_base_robot!25
* Change module number to 00
* Contributors: David ter Kuile, Noel Jimenez

2.0.8 (2024-04-10)
------------------
* Merge branch 'feat/enable-dlo-sim' into 'humble-devel'
  enable odom_tf gazebo only in public sim and laser noise fix
  See merge request robots/omni_base_robot!20
* enable odom_tf gazebo only in public sim and laser noise fix
* Contributors: andreacapodacqua

2.0.7 (2024-04-10)
------------------
* Add ros2controlcli dependency
* Contributors: Noel Jimenez

2.0.6 (2024-03-14)
------------------
* Merge branch 'dtk/feat/force-based-move-plugin' into 'humble-devel'
  Dtk/feat/force based move plugin
  See merge request robots/omni_base_robot!19
* linters
* disabled mobile_base_controller in simulation
* Contributors: andreacapodacqua

2.0.5 (2024-03-06)
------------------
* Merge branch 'feat/dlo-integration' into 'humble-devel'
  direct laser odometry integration
  See merge request robots/omni_base_robot!18
* direct laser odometry integration
* Contributors: andreacapodacqua

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
