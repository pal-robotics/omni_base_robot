^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package omni_base_bringup
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.10.1 (2025-04-09)
-------------------

2.10.0 (2025-03-25)
-------------------
* added tab_vel removed marker_vel
* Contributors: andreacapodacqua

2.9.0 (2025-02-24)
------------------
* updated maintainer
* update locks topics and teleop to integrate assisted_teleop
* Contributors: andreacapodacqua

2.8.0 (2025-01-23)
------------------
* support cobra and camera model
* Contributors: antoniobrandi

2.7.0 (2025-01-22)
------------------
* updated docking vel and lock topics
* lock robot if charging
* Contributors: antoniobrandi

2.6.0 (2025-01-16)
------------------

2.5.2 (2024-11-22)
------------------

2.5.1 (2024-11-08)
------------------

2.5.0 (2024-11-06)
------------------

2.4.2 (2024-10-18)
------------------

2.4.1 (2024-10-15)
------------------
* Merge branch 'fix/aca/joy-turbo' into 'humble-devel'
  using tiago config for joy turbo
  See merge request robots/omni_base_robot!45
* cosmetic
* using same configuration of TIAGo
* using tiago config for joy turbo
* Contributors: andreacapodacqua

2.4.0 (2024-09-04)
------------------
* Add slash to node names on parameter files
* Contributors: Noel Jimenez

2.3.0 (2024-08-29)
------------------
* use relay for cmd_vel message
* Contributors: David ter Kuile

2.2.0 (2024-08-08)
------------------
* start mobile_base_controller only for real robot
* Contributors: antoniobrandi

2.1.0 (2024-08-07)
------------------

2.0.19 (2024-07-09)
-------------------
* Add warning for pal_module_cmake not found
* Contributors: Noel Jimenez

2.0.18 (2024-07-01)
-------------------

2.0.17 (2024-06-28)
-------------------
* Merge branch 'dtk/add-on-module' into 'humble-devel'
  Change rgbd sensors to add-on-module
  See merge request robots/omni_base_robot!35
* Change rgbd sensors to add-on-module
* Contributors: David ter Kuile, davidterkuile

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
* Update linters
* Update arg name
* Add public sim
* Restructure luanch files omni_base_bringup
* Update to joy_linux node
* Contributors: David ter Kuile, davidterkuile

2.0.14 (2024-06-13)
-------------------

2.0.13 (2024-06-03)
-------------------

2.0.12 (2024-06-03)
-------------------

2.0.11 (2024-05-21)
-------------------

2.0.10 (2024-04-18)
-------------------

2.0.9 (2024-04-11)
------------------

2.0.8 (2024-04-10)
------------------
* Merge branch 'feat/enable-dlo-sim' into 'humble-devel'
  enable odom_tf gazebo only in public sim and laser noise fix
  See merge request robots/omni_base_robot!20
* enable odom_tf gazebo only in public sim and laser noise fix
* Contributors: andreacapodacqua

2.0.7 (2024-04-10)
------------------

2.0.6 (2024-03-14)
------------------

2.0.5 (2024-03-06)
------------------

2.0.4 (2024-02-26)
------------------

2.0.3 (2024-02-02)
------------------
* Merge branch 'feat/register-components' into 'humble-devel'
  removing need for remapping cmd_vel topic
  See merge request robots/omni_base_robot!16
* removing need for remapping cmd_vel topic
* Contributors: antoniobrandi

2.0.2 (2023-12-15)
------------------
* Merge branch 'fix/joystick-ros2' into 'humble-devel'
  added y-axis movement joystick
  See merge request robots/omni_base_robot!15
* added y-axis movement joystick
* Contributors: andreacapodacqua

2.0.1 (2023-12-11)
------------------
* Merge branch 'fix/modules-ros2' into 'humble-devel'
  fix modules
  See merge request robots/omni_base_robot!14
* fix cmakelists
* fix modules
* Contributors: Noel Jimenez, andreacapodacqua

2.0.0 (2023-11-22)
------------------
* Merge branch 'feat/module' into 'humble-devel'
  Feat/module
  See merge request robots/omni_base_robot!13
* fix deps
* fix dep
* split bringup module
* removed 2dnav dep
* update copyright
* omni_base ROS 2
* ROS 2 omni base robot
* add emergency brake priority
* disable controller and add TODO
* enable control(er) and 2dnav
* fix: Load gazebo_controller_manager_cfg.yaml and launch only omnibase stuff that is ready
* omnibase bringup to ROS 2:
  + yaml
  + launch.py
* omnibase bringup to colcon
* Contributors: YueErro, andreacapodacqua

0.0.10 (2022-12-27)
-------------------
* Merge branch 'fix/update-robot-state-publisher' into 'ferrum-devel'
  fix robot_state_publisher type
  See merge request robots/omni_base_robot!7
* fix robot_state_publisher type
* Contributors: josegarcia

0.0.9 (2022-10-24)
------------------

0.0.8 (2022-08-16)
------------------

0.0.7 (2022-08-10)
------------------

0.0.6 (2022-06-17)
------------------

0.0.5 (2021-11-24)
------------------

0.0.4 (2021-11-04)
------------------

0.0.3 (2021-10-05)
------------------
* fixed iso error while calling launch files for bringup
* Contributors: antoniobrandi

0.0.2 (2021-09-30)
------------------

0.0.1 (2021-09-30)
------------------
* preparing release changed version
* preparing release
* on of the urdf and completed controller configuration
* Contributors: antoniobrandi
