tekusbtmc
=========
*Python USBTMC driver for controlling Tektronix AFGs*

More information on the USBTMC protocol, programing and commands can be found in the [Tektronix AFG3000 Series Programmer Manual](http://www.tek.com/signal-generator/afg3000-manual/afg3000-series-2).

# Requirements
The *tekusbtmc* driver works without any additional package.

# Examples

## Open device

    from tekusbtmc import TekUsbtmc

    # open the first connected USBTMC device (/dev/usbtmc0)
    tek = TekUsbtmc()

or

    from tekusbtmc import TekUsbtmc

    # open the specific USBTMC device
    tek = TekUsbtmc("/dev/usbtmc0")

## Enable AFG output

    tek.write('OUTPut1:STATe ON')

## Upload waveform

The complete example can be found in the `example.py` file.

    # create some data to upload
    data = range(0,100)

    # upload data to USER1 waveform memory
    tek.upload_data(data, 'USER1')

### Upload from .mat file

The `example_mat.py` file provides the code for uploading a waveform to an AFG directly from a Matlab `.mat` file (required [scipy package](http://www.scipy.org/)). First the `create_waveform.m` file should be run in Matlab to create the `data.mat` file containing a multi-sine waveform. After that, the created waveform can be uploaded to an AFG with the `example_mat.py` file.
