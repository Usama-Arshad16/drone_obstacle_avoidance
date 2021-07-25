To run the package: 

- Extract the package to the catkin workspace.

- Source your catkin workspace, Open terminal window and commands: 
  $ cd catkin_ws
  $ catkin_make
  $ source devel/setup.bash 


-1 Launch Ar. Drone in Gazebo and rviz using the following command:
  $ roslaunch drone_gazebo drone.launch

-2 Enable the drone motors using command:
  $ rosservice call /enable_motors "enable: true"

-2 Run the following commands using a separate terminal:
  $ rosrun drone_control takeoff.py

- Wait to adjust hieght above 0.6 and below 0.8

-3 Run the following command in another terminal:
  $ roslaunch drone_navigation move_base.launch 
  


-4 Run the following command in another terminal:
  $ rosrun drone_control goal.py


