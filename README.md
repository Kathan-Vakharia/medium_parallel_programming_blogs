# Amdahl's Law: Why More Workers ≠ Faster Projects

## 🎯 What This Shows

A visual demonstration of **Amdahl's Law** - the fundamental principle that explains why throwing more people at a project doesn't always speed it up.

## 📊 The Scenario

- **Base case**: 20 workers complete a project in 36 months (720 worker-months total)
- **Question**: What happens when we add more workers?
- **Answer**: It depends on how much work can be done in parallel!

## 🔑 Key Concepts

### Sequential vs Parallel Work

- **Sequential Work**: Must be done in order by a core team
  - Examples: Getting permits, final inspections, code reviews
  - Time: Fixed regardless of total workforce size
  
- **Parallel Work**: Can be divided among many workers
  - Examples: Construction, coding features, testing
  - Time: Decreases as you add more workers

### The Formula
```
Total Time = Sequential Time + Parallel Time
           = (Sequential Work ÷ Core Team) + (Parallel Work ÷ Total Workers)
```

## 📈 What the Chart Reveals

**Green Line (10% Sequential)**: Adding workers helps a lot - most work can be parallelized
**Red Line (90% Sequential)**: Adding workers barely helps - sequential bottleneck dominates

## 💡 The Big Insight

**Amdahl's Law proves that the sequential portion of any task sets a hard limit on how much speedup is possible, no matter how many resources you add.**

Even with infinite workers:
- 10% sequential work → Maximum 10x speedup
- 90% sequential work → Maximum 1.1x speedup

where $Maximum Speedup = \frac{1}{Sequential Fraction}$

## 🌍 Real-World Applications

- **Software Development**: Why large teams don't always ship faster
- **Manufacturing**: Why some production lines can't be infinitely parallelized  
- **Project Management**: Why critical path tasks matter more than team size
- **Computing**: Why parallel processing hits diminishing returns

## 🚀 Running the Code

```bash
python amdahl_visualization.py
```

The script generates an interactive visualization showing how project completion time varies with team size for different sequential/parallel work ratios.
