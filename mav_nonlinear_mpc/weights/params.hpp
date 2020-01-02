#include <Eigen/Dense>
#include <iostream>
#include "mc_weights.c"
#include "mc_bias.c"
using namespace Eigen;

class weights
{
public:
	Eigen::Matrix<float,LAYER_1_WEIGHT_ROWS, LAYER_1_WEIGHT_COLS> layer_1_weight;
	Eigen::Matrix<float,LAYER_2_WEIGHT_ROWS, LAYER_2_WEIGHT_COLS> layer_2_weight;
	Eigen::Matrix<float,LAYER_3_WEIGHT_ROWS, LAYER_3_WEIGHT_COLS> layer_3_weight;
	
	weights (){
		layer_1_weight << LAYER_1_WEIGHT;
		layer_2_weight << LAYER_2_WEIGHT;
		layer_3_weight << LAYER_3_WEIGHT;
	}
};
