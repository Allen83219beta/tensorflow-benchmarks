import argparse
import os
import subprocess
import sys

def main(checkpoint_path, model, num_trials):
  print("Number of images\tInference time")
  num_trials = 1000
  for batch_size in [2048, 4096, 8192]:
    command = ("python tf_cnn_benchmarks.py --model=%(model)s --eval --data_dir=/lfs/1/deepak/data/imagenet/ --eval_subset=validation --num_batches=%(num_trials)d --batch_size=%(batch_size)d" %
               {"model": model, "batch_size": batch_size, "num_trials": num_trials})
    full_command = command + " --checkpoint_dir=%s 2>/dev/null" % checkpoint_path
    try:
      output = subprocess.check_output(full_command, shell=True)
      output = output.decode('utf8').strip()
      for line in output.split('\n'):
        if "Time for inference" in line:
          line = line.strip()
          inference_time = float(line.split(": ")[1])
          inference_time = inference_time / num_trials
          stats = [batch_size, inference_time]
          print("\t".join([str(stat) for stat in stats]))
          sys.stdout.flush()
    except:
      stats = [batch_size, ""]
      print("\t".join([str(stat) for stat in stats]))
      sys.stdout.flush()


if __name__ == '__main__':
  parser = argparse.ArgumentParser(
    description=("Backup model checkpoints periodically")
  )
  parser.add_argument('-i', "--checkpoint_path", type=str, required=True,
                      help="Path to dumped model checkpoints")
  parser.add_argument('-m', "--model", type=str, required=True,
                      help="Model name")
  parser.add_argument('-n', "--num_trials", type=int, default=100,
                      help="Number of trials")

  cmdline_args = parser.parse_args()
  opt_dict = vars(cmdline_args)

  checkpoint_path = opt_dict["checkpoint_path"]
  model = opt_dict["model"]
  num_trials = opt_dict["num_trials"]

  main(checkpoint_path, model, num_trials)
