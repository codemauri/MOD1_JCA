import statistics

def mean(data):
    return sum(data) / len(data)

def median(data):
    sorted_data = sorted(data)
    n = len(data)
    if n % 2 == 1:
        return sorted_data[n // 2]
    else:
        return (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2

def std_dev(data):
    n = len(data)
    if n < 2:
        raise ValueError("stdev requires at least two data points")
    mean = sum(data) / n
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    return variance ** 0.5



def calculate(data):
    # mean = statistics.mean(data)
    # median = statistics.median(data)
    # std_dev = statistics.stdev(data)
    meanv = mean(data)
    medianv = median(data)
    std_devv = std_dev(data)

    return round(meanv, 2), round(medianv,2) ,round(std_devv,2)

def output(results):
    print(f"{'':<10} {'Fall 2016':>10} {'Spring 2016':>15}")
    print(f"{'Mean':<10} {results['Fall 2016']['Mean']:>10.2f} {results['Spring 2016']['Mean']:>15.2f}")
    print(f"{'Median':<10} {results['Fall 2016']['Median']:>10.2f} {results['Spring 2016']['Median']:>15.2f}")
    print(f"{'STD':<10} {results['Fall 2016']['STD']:>10.2f} {results['Spring 2016']['STD']:>15.2f}")


def function2():
    fall = []
    spring = []
    results = {}
    csvfile = "sample_grades.csv"
    dataIn = open(csvfile, "r")
    for line in dataIn:
        parts = line.split(",")
        if parts[1] == "Spring 2016":
            spring.append(float(parts[2]))
        else:
            fall.append(float(parts[2]))
    dataIn.close()
    meanF, medianF, std_devF = calculate(fall)
    meanS, medianS, std_devS = calculate(spring)
    results["Fall 2016"] = {"Mean": meanF, "Median": medianF, "STD": std_devF}
    results["Spring 2016"] = {"Mean": meanS, "Median": medianS, "STD": std_devS}
    output(results)




def main():
    function2()

main()