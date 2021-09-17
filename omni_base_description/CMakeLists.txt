cmake_minimum_required(VERSION 2.8.3)
project(omni_base_description)

find_package(catkin REQUIRED)

catkin_package()

foreach(dir gazebo  meshes robots urdf config)
    install(DIRECTORY ${dir}/
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}/${dir})
endforeach(dir)

#############
## Testing ##
#############

if(CATKIN_ENABLE_TESTING)
    find_package(rostest REQUIRED)
    add_rostest(test/test_omni_base.test)
endif()
