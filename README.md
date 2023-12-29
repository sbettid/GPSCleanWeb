# GPSClean Web

GPSClean Web is a small web interface for the model resulting used by [GPSClean](https://github.com/sbettid/GPSClean).

        
GPSClean is the result of research conducted as Master Thesis at the Free University of Bolzano-Bozen, and concentrates in showing
how it is possible to effectively correct GPS traces from measurements mistakes without the use of geographical information, 
such as the location in which the trace was recorded. 
        
In a nutshell, each GPS trace is processed as follows:
        
1. Each point of the trace is classified, according to a trained machine learning model, in one of the following categories
            
    - Correct Point
    - Pause (so a recorded movement while the real position was stationary)
    - Wrongly position point

2. Pauses are removed and replaced with the average of their positions
3. Wrongly positioned points are replaced with the result of the application of a 
    double [Kalman Filter](https://en.wikipedia.org/wiki/Kalman_filter) (which we named "Bi-Directional Kalman Filter)
4. The corrected trace is exported back in the widely adopted GPX format
        
Would you like to know more about GPSClean and the research behind it? \
Then feel free to consult the 
project's [GitHub page](https://github.com/sbettid/GPSClean) or read the [associated paper](https://www.thinkmind.org/index.php?view=article&articleid=signal_2022_1_10_60003). 