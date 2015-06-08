#include <pcl/point_types.h>
#include <pcl/features/normal_3d.h>
#include <pcl/io/pcd_io.h> //para error en LOAD PCD FILE 
#include <pcl/visualization/cloud_viewer.h>
#include <iostream>

int 
main () 
{ 
  pcl::PointCloud<pcl::PointXYZ>::Ptr cloud (new pcl::PointCloud<pcl::PointXYZ>); 
  pcl::io::loadPCDFile ("Points.pcd", *cloud); 
  
  // Create the normal estimation class, and pass the input dataset to it 
  pcl::NormalEstimation<pcl::PointXYZ, pcl::Normal> ne; 
  ne.setInputCloud (cloud); 

  // Output datasets 
  const pcl::PointCloud<pcl::Normal>::Ptr cloud_normals (new pcl::PointCloud<pcl::Normal>); 

  // Use all neighbors in a sphere of radius 3cm 
  ne.setRadiusSearch (100); 

  // Compute the features 
  ne.compute (*cloud_normals); 

  // cloud_normals->points.size () should have the same size as the input cloud->points.size () 

  // visualize normals 
  //      pcl::visualization::PCLVisualizer viewer("PCL Viewer"); 
  //      viewer.setBackgroundColor (0.0, 0.0, 0.5); 
        
  //      viewer.addPointCloudNormals<pcl::PointXYZ,pcl::Normal>(cloud, cloud_normals); 
  //      while (!viewer.wasStopped ()) 
  //      { 
  //              viewer.spinOnce (); 
  //      } 
        

        pcl::io::savePCDFileASCII ("Normals.pcd", *cloud_normals); 
        return 0; 
} 