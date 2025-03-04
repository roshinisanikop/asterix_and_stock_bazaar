
latency_file = "latency_results.txt"
def compute_overall_avg():
    with open(latency_file, "r") as f:
        # latencies=[]
        # for l in f.readlines():
        #     latencies.append(float(l.strip()))
        latencies = [float(line.strip()) for line in f.readlines()]
    
        overall_avg = sum(latencies)/len(latencies)
        print(f"overall average latency across {len(latencies)} clients is: {overall_avg:.4f} seconds")

if __name__ == "__main__":
    compute_overall_avg()