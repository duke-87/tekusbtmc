% This script creates data.mat file, which contains a simple waveform
clear all
close all


freq= [1 2];
ts = 0.001;
t = (0:999)*ts;

% multi sinus waveform:
waveform = sin(2*pi.*freq(1).*t) + sin(2*pi.*freq(2).*t);

% scale the waveform to fit the AFG requirements (0--16382)
waveform = waveform - min(waveform);
waveform = waveform/max(waveform);
waveform = round(waveform*16382);

%plot(t, waveform, '-*')

save data waveform
max(waveform)
min(waveform)
