import os, sys

# RM1

num_epochs  = 1
num_batches = 400

rt_config_cpu = "--inference_only --inter_op_workers 4 --caffe2_net_type async_dag "
rt_config_gpu = "--inference_only --inter_op_workers 1 --caffe2_net_type async_dag --use_gpu "

model_config = "--model_type dlrm --arch_mlp_top \"256-64-1\" --arch_mlp_bot \"128-64-32\" --arch_sparse_feature_size 32 --arch_embedding_size \"1000000-1000000-1000000-1000000-1000000-1000000-1000000-1000000\" --num_indices_per_lookup 80 --num_indices_per_lookup_fixed True --arch_interaction_op cat "

# Sweep Batch Size from {2^0 = 1, ... ,2^14 = 16384}
sls_type = "base"
for x in range(8):
	n = 2**x
        #n = 32
	data_config = "--nepochs " + str(num_epochs) + " --num_batches " + str(num_batches) + " --mini_batch_size " + str(n) + " --max_mini_batch_size " + str(n) + " --sls_type " + str(sls_type) + " --data_generation synthetic"

	cpu_command = "python dlrm_s_caffe2.py " + rt_config_cpu + model_config + data_config
	gpu_command = "python dlrm_s_caffe2.py " + rt_config_gpu + model_config + data_config

	print("--------------------Running (RM1) CPU Test with Batch Size " + str(n) +"--------------------\n")
	print(cpu_command)
	#os.system(cpu_command)
	# print("--------------------Running (RM1) GPU Test with Batch Size " + str(n) +"--------------------\n")
	# print(gpu_command)
	# os.system(gpu_command)
