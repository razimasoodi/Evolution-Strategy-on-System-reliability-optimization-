# Evolution-Strategy-on-System-reliability-optimization
System reliability optimization is very important in real world applications. To design a highly
reliable system, there are two main approaches: 1) Add redundant components 2) Increases
the component reliability.
For financial reasons, it has to establish a balance between reliability and other resources
during designing a highly reliable system. In this project we ask you to design an Evolution
Strategy (ES) based approach to reach this goal.
Well-known benchmarks
The notations used in this project are listed in table (1):
table 1: notations

![Screenshot (104)](https://github.com/razimasoodi/Evolution-Strategy-on-System-reliability-optimization-/assets/170275013/b83cca26-3d57-40b1-9b13-56624a7db0e1)

The reliability–redundancy allocation problem can be modeled in general form as follow:

Max Rs = f (ri, ni).

subject to g (ri, ni) ≤ predefinedValue

Where f (.) is the objective function (fitness function) for the overall system and g(.) is the set
of constraint functions (e.g., constraints are on system weight, volume and cost). For more
information, see:
P. Wu, L. Gao, D. Zou, and S. Li, “An improved particle swarm optimization algorithm for
reliability problems,” ISA Trans., vol. 50, no. 1, pp. 71–81, 2011.

1.1. Complex (bridge) system (P1): Figure 1 represent a complex system that consists of five
subsystems. The objective function for complex system is:

𝑀𝑎𝑥 𝑓(𝑟. 𝑛𝑐)= 𝑅1𝑅2 + 𝑅3𝑅4+ 𝑅1𝑅4𝑅5 + 𝑅2𝑅3𝑅5− 𝑅1𝑅2𝑅3𝑅4 - 𝑅1𝑅2𝑅3𝑅5− 𝑅1𝑅2𝑅4𝑅5 − 𝑅1𝑅3𝑅4𝑅5 − 𝑅2𝑅3𝑅4𝑅5 + 2𝑅1𝑅2𝑅3𝑅4𝑅5

subject to:

![image](https://github.com/razimasoodi/Evolution-Strategy-on-System-reliability-optimization-/assets/170275013/29f3d035-58d6-43cf-b135-798157893282)

1.2. Series system (P2): Figure 2 represents a series system consisting of five subsystems. The
objective function for series system is:

𝑀𝑎𝑥 𝑓(𝑟. 𝑛)= Π𝑅𝑖𝑚𝑖=1= Π(1 − (1 −𝑟 𝑖)𝑛𝑖5𝑖=1

subject to: 𝑔1(𝑟. 𝑛) . 𝑔2(𝑟. 𝑛), 𝑔3(𝑟. 𝑛).

Parameter used for complex (bridge) system (P1) and series system (P2) are listed in table(2):

Table 2. Parameter used for complex and series system
![image](https://github.com/razimasoodi/Evolution-Strategy-on-System-reliability-optimization-/assets/170275013/026079b2-8285-42a3-914e-ee6451a2f3d7)
![Screenshot (105)](https://github.com/razimasoodi/Evolution-Strategy-on-System-reliability-optimization-/assets/170275013/c5d79d6e-e724-4820-ad59-5789100ae05f)


