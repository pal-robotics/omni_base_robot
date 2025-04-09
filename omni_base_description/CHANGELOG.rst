^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package omni_base_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

2.10.1 (2025-04-09)
-------------------
* Merge branch 'tpe/imu_fix' into 'humble-devel'
  Pass the name to the IMU plugin in case we have several IMUs
  See merge request robots/omni_base_robot!63
* Pass the name to the IMU plugin in case we have several IMUs
* Contributors: thomas.peyrucain, thomaspeyrucain

2.10.0 (2025-03-25)
-------------------

2.9.0 (2025-02-24)
------------------
* updated maintainer
* Contributors: andreacapodacqua

2.8.0 (2025-01-23)
------------------
* support cobra and camera model
* Contributors: antoniobrandi

2.7.0 (2025-01-22)
------------------

2.6.0 (2025-01-16)
------------------
* Merge branch 'tpe/simplify-3d-model' into 'humble-devel'
  Simplify 3d meshes
  See merge request robots/omni_base_robot!54
* Simplify 3d meshes
* Contributors: thomas.peyrucain, thomaspeyrucain

2.5.2 (2024-11-22)
------------------

2.5.1 (2024-11-08)
------------------
* Remove add_module_on from test
* Add xacro tests
* Contributors: Aina

2.5.0 (2024-11-06)
------------------

2.4.2 (2024-10-18)
------------------
* Merge branch 'tpe/fix_base_inertia' into 'humble-devel'
  Remove unwanter base inertia
  See merge request robots/omni_base_robot!46
* Remove unwanter base inertia
* Contributors: thomas.peyrucain, thomaspeyrucain

2.4.1 (2024-10-15)
------------------

2.4.0 (2024-09-04)
------------------
* Add slash to node names on parameter files
* Contributors: Noel Jimenez

2.3.0 (2024-08-29)
------------------

2.2.0 (2024-08-08)
------------------

2.1.0 (2024-08-07)
------------------

2.0.19 (2024-07-09)
-------------------
* Add warning for pal_module_cmake not found
* Contributors: Noel Jimenez

2.0.18 (2024-07-01)
-------------------
* Merge branch 'dtk/disable-rgbd-test' into 'humble-devel'
  Disable realsense test
  See merge request robots/omni_base_robot!36
* Disable realsense test
* Contributors: David ter Kuile, davidterkuile

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
* Restructure gazebo urdf
* Update linters
* Add public sim
* Remove colons from urdf to avoid crash of ros2 control gazebo
* Update launch arguments omni_base_description
* Update URDF structure
* Fix argument + tests
* Standardize urdf + update lauch args
* Contributors: David ter Kuile, davidterkuile, thomas.peyrucain

2.0.14 (2024-06-13)
-------------------
* Merge branch 'fix/robot_state_publisher' into 'humble-devel'
  fix robot state publisher launch file
  See merge request robots/omni_base_robot!33
* specify robot description as string
* fix robot state publisher launch file
* Contributors: Aina, davidterkuile

2.0.13 (2024-06-03)
-------------------

2.0.12 (2024-06-03)
-------------------
* Merge branch 'fix/aca/reduced-laser-noise' into 'humble-devel'
  reduced laser_noise
  See merge request robots/omni_base_robot!30
* reduced laser_noise
* Contributors: andreacapodacqua

2.0.11 (2024-05-21)
-------------------
* Merge branch 'feat/aca/realsense-ros2' into 'humble-devel'
  added realsense support
  See merge request robots/omni_base_robot!28
* Revert "swap camera names"
  This reverts commit 10b11403fde04f52c57782ff8e30f3e92cd042cc.
* swap camera names
* removed simulation arg and fix use_nominal_extrinsic
* added rgbd_sensors to module
* added realsense support
* Merge branch 'fix/is_public_sim_argument' into 'humble-devel'
  add missing argument is_public_sim
  See merge request robots/omni_base_robot!29
* add missing argument is_public_sim
* Contributors: Aina Irisarri, andreacapodacqua, davidterkuile

2.0.10 (2024-04-18)
-------------------
* Merge branch 'fix/ros2-missing-deps' into 'humble-devel'
  adding missing deps
  See merge request robots/omni_base_robot!26
* adding missing deps
* Contributors: Noel Jimenez, andreacapodacqua

2.0.9 (2024-04-11)
------------------
* Merge branch 'omm/feat/planar_move_plugin' into 'humble-devel'
  Restored old plugin with is_public_sim checks
  See merge request robots/omni_base_robot!24
* Removing hector plugin dep
* Restored old gazebo plugin
* Merge branch 'dtk/fix/update-module-numbers' into 'humble-devel'
  Dtk/fix/update module numbers
  See merge request robots/omni_base_robot!25
* Change module number to 00
* Merge branch 'dtk/fix/remove-pmb2-dependency' into 'humble-devel'
  Remove pmb2-description dependency
  See merge request robots/omni_base_robot!22
* Remove dependency of pmb2
* Remove pmb2-description dependency
* Contributors: David ter Kuile, Noel Jimenez, Oscar, andreacapodacqua, davidterkuile

2.0.8 (2024-04-10)
------------------
* Merge branch 'feat/enable-dlo-sim' into 'humble-devel'
  enable odom_tf gazebo only in public sim and laser noise fix
  See merge request robots/omni_base_robot!20
* restored default laser noise
* enable odom_tf gazebo only in public sim and laser noise fix
* Contributors: andreacapodacqua

2.0.7 (2024-04-10)
------------------

2.0.6 (2024-03-14)
------------------
* Merge branch 'dtk/feat/force-based-move-plugin' into 'humble-devel'
  Dtk/feat/force based move plugin
  See merge request robots/omni_base_robot!19
* Create a pal_distro dependency to not break humble ci untill pr gets accepted
* Add hector gazebo plugin dependency
* Remove namespace for multirobot
* Change to force_based_move from hector gazebo plugins
* Remove friction of the wheels, similar to as in ROS1
* Contributors: David ter Kuile, andreacapodacqua, davidterkuile

2.0.5 (2024-03-06)
------------------

2.0.4 (2024-02-26)
------------------

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
* fix modules
* Contributors: Noel Jimenez, andreacapodacqua

2.0.0 (2023-11-22)
------------------
* Merge branch 'feat/module' into 'humble-devel'
  Feat/module
  See merge request robots/omni_base_robot!13
* using correct name
* split bringup module
* Merge branch 'fix/use_sim_time' into 'humble-devel'
  Set use_sim_time false as default
  See merge request robots/omni_base_robot!12
* Set use_sim_time false as default
* update copyright
* fix: planar move plugin
* omni_base ROS 2
* fix lidar mesh issues and using light base stl
* fix: planar move plugin parameters
* fix: replace force_based_move by planar_move
* add imu_sensor_broadcaster fix robot_model
* ROS 2 omni base robot
* Add TODO to gazebo.urdf.xacro force based move plugin
* enable control(er) and 2dnav
* fix: Load gazebo_controller_manager_cfg.yaml and launch only omnibase stuff that is ready
* omnibase description to ROS 2:
  + xacro
  + ros2_control
  + launch.py
* omnibase description to colcon
* Contributors: Noel Jimenez, YueErro, andreacapodacqua, josegarcia

0.0.10 (2022-12-27)
-------------------

0.0.9 (2022-10-24)
------------------

0.0.8 (2022-08-16)
------------------
* Merge branch 'fix/laser-fov' into 'ferrum-devel'
  fix laser fov for omni base
  See merge request robots/omni_base_robot!4
* fix laser fov for omni base
* Contributors: antoniobrandi

0.0.7 (2022-08-10)
------------------
* Merge branch 'fix_base_collision' into 'ferrum-devel'
  Fix collision boxes for the base
  See merge request robots/omni_base_robot!3
* Update box dimensions
* Change suspension_side_joints to fixed joint because it was causing issue in the odometry
* Fix collision boxes for the base
* Contributors: saikishor, thomaspeyrucain

0.0.6 (2022-06-17)
------------------
* Merge branch 'hokuyo-support' into 'ferrum-devel'
  Fix typo in macro
  See merge request robots/omni_base_robot!2
* Fix typo in macro
* Contributors: David ter Kuile, antoniobrandi

0.0.5 (2021-11-24)
------------------
* Using the full mesh instead of the two boxes
* added dependency for hector
* removed dependency
* Changed ros_planar_move for ros_force_based_move
* Split the collision into 2 boxes for the sake of laser
* Update the collision model of the base_link
* Contributors: Sai Kishor Kothakota, antoniobrandi, saikishor

0.0.4 (2021-11-04)
------------------
* typo
* Contributors: antoniobrandi

0.0.3 (2021-10-05)
------------------

0.0.2 (2021-09-30)
------------------
* removed useless dependency to omni_base_description_calibration
* Contributors: antoniobrandi

0.0.1 (2021-09-30)
------------------
* preparing release changed version
* preparing release
* Fixing wheel naming convention using rear instead of back
* Merge branch 'omni_base_sw' into 'master'
  Omni base sw
  See merge request robots/omni_base_robot!1
* fix the min and max angle of the lasers
* added the virtual base laser link
* fix the laser model naming for front and rear sensors
* added missing deg_to_rad xacro
* update the new wheel macro in the main URDF
* update the wheel urdf xacro with the updated info from solidworks
* remove unused base_laser_link
* added new wheel meshes
* update the information of the front-right and rear-left laser sensor
* added base docking link frame
* added antenna's links and meshes
* update the wheel separation, radius and width parameters
* update the base_link mesh and the link information
* Changed laser scan topic for the simulation navigation
* on of the urdf and completed controller configuration
* Contributors: Sai Kishor Kothakota, antoniobrandi
