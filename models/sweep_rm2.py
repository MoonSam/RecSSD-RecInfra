import os, sys

# RM2

num_epochs  = 1
num_batches = 400

rt_config_cpu = "--inference_only --inter_op_workers 4 --caffe2_net_type simple --enable_profiling "
rt_config_gpu = "--inference_only --inter_op_workers 1 --caffe2_net_type simple --use_gpu --enable_profiling "

model_config = "--model_type dlrm --arch_mlp_top \"128-64-1\" --arch_mlp_bot \"128-64-64\" --arch_sparse_feature_size 64 --arch_embedding_size \"1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000\" --num_indices_per_lookup 120 --num_indices_per_lookup_fixed True --arch_interaction_op cat "

# Sweep Batch Size from {2^0 = 1, ... ,2^14 = 16384}
sls_type = "ndp"
for x in range(6):
	n = 2**x
        #n = 32
	data_config = "--nepochs " + str(num_epochs) + " --num_batches " + str(num_batches) + " --mini_batch_size " + str(n) + " --max_mini_batch_size " + str(n) + " --sls_type " + str(sls_type) + " --data_generation synthetic"

	cpu_command = "python dlrm_s_caffe2.py " + rt_config_cpu + model_config + data_config
	gpu_command = "python dlrm_s_caffe2.py " + rt_config_gpu + model_config + data_config

	print("--------------------Running (RM2) CPU Test with Batch Size " + str(n) +"--------------------\n")
	print(cpu_command)
	#os.system(cpu_command)
	#print("--------------------Running (RM2) GPU Test with Batch Size " + str(n) +"--------------------\n")
	# print(gpu_command)
	#os.system(gpu_command)
