# IEPF Line Extraction Algorithm

IEPF (*Iterative End Point Fit*) Line Extraction

Simple program to implement IEPF line extraction in Python

The algorithm will produce N line function: 

![equation](/Images/Equation1.png)

## Dependencies

* Python 2.7
* Matplotlib

## Demo Program

* **Red dot** is N point which produced by simple line function with additional noise. Normally this point represent sensor reading like sonar, lidar, or depth camera
* **Blue line** is estimate line which produced by IEPF algorithm

![IEPF Line Extraction Demo 1](/Images/Demo1.png)

![IEPF Line Extraction Demo 1](/Images/Demo2.png)

## References

* [Nguyen, Viet, et al. "A comparison of line extraction algorithms using 2D laser rangefinder for indoor mobile robotics." Intelligent Robots and Systems, 2005.(IROS 2005). 2005 IEEE/RSJ International Conference on. IEEE, 2005.](http://ieeexplore.ieee.org/abstract/document/1545234/)
* [Einsele, Tobias. "Real-time self-localization in unknown indoor environment using a panorama laser range finder." Intelligent Robots and Systems, 1997. IROS'97., Proceedings of the 1997 IEEE/RSJ International Conference on. Vol. 2. IEEE, 1997.](http://ieeexplore.ieee.org/abstract/document/655087/)
* [Lv, Jixin, et al. "Straight line segments extraction and ekf-slam in indoor environment." Journal of Automation and Control Engineering 2.3 (2014).](https://www.researchgate.net/profile/Ankit_Ravankar/publication/259935653_Straight_Line_Segments_Extraction_and_EKF-SLAM_in_Indoor_Environment/links/0f31752ea3aa10f8fc000000.pdf)
