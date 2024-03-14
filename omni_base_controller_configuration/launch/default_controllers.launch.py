# Copyright (c) 2023 PAL Robotics S.L. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from launch import LaunchDescription
from launch.conditions import  LaunchConfigurationNotEquals
from launch_pal.include_utils import include_launch_py_description


def generate_launch_description():

    mobile_base_controller_launch = include_launch_py_description(
        'omni_base_controller_configuration', ['launch', 'mobile_base_controller.launch.py'],
        condition=LaunchConfigurationNotEquals('use_sim_time', 'True'))

    joint_state_broadcaster_launch = include_launch_py_description(
        'omni_base_controller_configuration', ['launch', 'joint_state_broadcaster.launch.py'])

    
    
    imu_sensor_broadcaster_launch = include_launch_py_description(
        'omni_base_controller_configuration', ['launch', 'imu_sensor_broadcaster.launch.py'])

    ld = LaunchDescription()

    ld.add_action(mobile_base_controller_launch)
    ld.add_action(joint_state_broadcaster_launch)
    ld.add_action(imu_sensor_broadcaster_launch)

    return ld
