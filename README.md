# rlkk
Regularized Linear Kramers-Kronig (rLKK)

|Folder | Implementation | Info | Version |
| MATLAB | Matlab (function) | recommended function version | v5 |
| MATLAB-script | Matlab (script) | for workflows in matlab | v5 |
| Python | Python + Jupyter | For Python implementations | v5 |

## Why rLKK?
rLKK can be used to evaluate the impedance spectrum data. 

Given frequency vector "f" and complex impedance vector "Z"

rLKK constructs a new impedance spectrum "Zf"

If the deviation between "Zf" and "Z" is small (rule of thumb 1% or 2%), the measurement is validated (meaning it came from causal, linear and time-invariant conditions)

Otherwise, all points larger should either be eliminated or remeasured

More details: Kanoun, Olfa, and Ahmed Yahia Kallel. "High-performance efficient embedded systems for impedance spectroscopy: Challenges and potentials." Electrochimica Acta (2024): 144351.


rLKK can be used to 'correct' impedance spectrum

Condition: the nature of deviation is "white", meaning the deviation is centered around 0% 

In general thermal and quantization noise satisfy this condition

rLKK must be used with extreme caution otherwise!



## Use
rLKK requires a complex impedance spectrum "Z" and frequency vector "f"

it uses an internal "DRT frequency vector" (fx) which should be larger than measurement frequency "f" and encapsulate the different phenomena being measured

in addition, it uses a "regularization factor" (lambda): lambda should be around 10^-2 (10^-1 to 10^-6). larger lambda = more distortions and the algorithm should put more effort as measurements aren't reliable

If not sure, leave it as it is


## Implementations
Current support: MATLAB, Python (Jupyter), Python


As of the moment, rLKK is implemented in MATLAB (Script and Function)

These are used since 2021 in MST, TU Chemnitz, internally and are validated multiple times

They are also "Octave" (Open Source)-compatible

The Python code is relatively new, and is used in MST

Graphical interface version is coming soon!


## Cite and use case
Recommendation to cite this paper, if you have ever used rLKK

 [Kallel2021] Kallel, Ahmed Yahia, and Olfa Kanoun. "Regularized linear kramers-kronig transform for consistency check of noisy impedance spectra with logarithmic frequency distribution." 2021 International Workshop on Impedance Spectroscopy (IWIS). IEEE, 2021.

As for why rLKK is better than conventional LKK and LKK-iterative is discussed in my Ph.D. Thesis, and in the following open access paper:

[Kanoun2024] Kanoun, Olfa, and Ahmed Yahia Kallel. "High-performance efficient embedded systems for impedance spectroscopy: Challenges and potentials." Electrochimica Acta (2024): 144351.
rLKK makes sense to use more than the other methods because regularization is an established method to avoid influence from noise and distortions and all I did is to bring it to LKK testing.


Where rLKK was used and use case (live page):

https://scholar.google.de/scholar?oi=bibs&hl=de&cites=2453183610233729588

## License
Licensed under MIT 