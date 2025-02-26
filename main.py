from dis import dis
import cv2
import numpy as np
from tools import *
from random import randint
from calibration_intrinsic import obtain_intrinsic
from calibration_extrinsic import obtain_extrinsic
from call_one import obtain_extrinsic1
from call_two import obtain_extrinsic2

if __name__ == '__main__':
    ## 0、内外参  防辐射相机 - 焦距30cm，格子边长12mm
    l = 12.

    camera_matrix, dist_matrix, error = obtain_intrinsic(
        r"D:\1", l)

    print(camera_matrix)
    print(dist_matrix)

    # R_ex, t_ex1 = obtain_extrinsic(r"C:\Users\31047\Desktop\PYP\ccc\325__345", camera_matrix,di/st_matrix, l)
    R_ex, t_ex1 = obtain_extrinsic(r"D:\2\124", camera_matrix, dist_matrix, l)
    # R_ex, t_ex1 = obtain_extrinsic2(r"C:\Users\31047\Desktop\325__345", camera_matrix, dist_matrix, l)



    # new_arrays = [word_points[i:i + 24] for i in range(0, len(word_points), 24)]
    # new_array1 = [element[:2] for element in new_arrays[0]]
    # new_array2 = [element[:2] for element in new_arrays[1]]
    # th3_elements = []
    #
    # # 遍历大数组中的每个小数组
    # for small_array in new_arrays[0]:
    #     # 检查当前小数组是否有足够的元素
    #     # 获取小数组的第三个元素，并添加到third_elements列表中
    #     third_element = small_array[2]
    #     th3_elements.append(third_element)
    #
    # def triangulate_points(points1, points2, camera_matrix, R, t):
    #     # 生成投影矩阵
    #     projection_matrix1 = np.hstack((camera_matrix, np.zeros((3, 1))))
    #     projection_matrix2 = np.hstack((R, t))
    #
    #     # 转换点坐标为齐次坐标
    #     points1_homogeneous = np.vstack((points1.T, np.ones(points1.shape[0])))
    #     points2_homogeneous = np.vstack((points2.T, np.ones(points2.shape[0])))
    #
    #     # 进行三角测量
    #     points_4d_homogeneous = cv2.triangulatePoints(projection_matrix1, projection_matrix2, points1_homogeneous[:2],
    #                                                   points2_homogeneous[:2])
    #
    #     # 将齐次坐标转换为三维坐标
    #     points_3d = cv2.convertPointsFromHomogeneous(points_4d_homogeneous.T).squeeze()
    #
    #     return points_3d
    #
    #
    # # 进行三角测量
    # points1 =new_array1
    # points2 =new_array2
    # points1 = np.array(points1)
    # points2 = np.array(points2)
    #
    # points_3d = triangulate_points(points1,points2,camera_matrix,R_ex,t_ex1)
    # # 输出三维坐标
    # print("wocccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc")
    # print(points_3d)#相机坐标下的三维坐标
    # third_elements = [sub_array[2] for sub_array in points_3d]
    # # print("third_numbers", third_elements )
    # print("mean_third_numbers",np.mean(third_elements))
    # print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    # print("与实际距离相差了",abs(10*th3_elements[0]-abs(np.mean(third_elements))),"毫米")


