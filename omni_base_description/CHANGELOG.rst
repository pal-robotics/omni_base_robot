^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Changelog for package omni_base_description
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

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
