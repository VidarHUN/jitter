# Quick note about AMR

- AMR - Adaptive Multi-Rate audio codec
- AMR-WB Adaptive Multi-Rate Wideband audio codec
- Used for speech 

The payload format supports transmission of multiple channels, 
multiple frames per payload, the use of fast codec mode adaptation, 
robustness against packet loss and bit errors, and interoperation 
with existing AMR and AMR-WB transport formats on non-IP networks.

AMR and AMR-WB were originally designed for circuit-switched mobile 
radio systems.  Due to their flexibility and robustness, they are
also suitable for other real-time speech communication services over
packet-switched networks such as the Internet.


## AMR

The AMR codec was originally developed and standardized by the
European Telecommunications Standards Institute (ETSI) for GSM
cellular systems.  It is now chosen by the Third Generation
Partnership Project (3GPP) as the mandatory codec for third
generation (3G) cellular systems.

The AMR codec is a multi-mode codec that supports eight narrow band
speech encoding modes with bit rates between 4.75 and 12.2 kbps.  The
sampling frequency used in AMR is **8000 Hz** and the speech encoding is
performed on **20 ms speech frames**.  Therefore, each encoded AMR speech
frame represents **160 samples** of the original speech.

## Voice Activity Detection and Discontinuous Transmission

Both codecs support voice activity detection (VAD) and generation of
comfort noise (CN) parameters during silence periods.  Hence, the
codecs have the option to reduce the number of transmitted bits and
packets during silence periods to a minimum. The operation of
sending CN parameters at regular intervals during silence periods is
usually called discontinuous transmission (DTX) or source controlled
rate (SCR) operation.  The AMR or AMR-WB frames containing CN
parameters are called Silence Indicator (SID) frames.

## RTP header usage

The RTP header marker bit (M) SHALL be set to 1 if the first frame-
block carried in the packet contains a speech frame which is the
first in a talkspurt.  For all other packets the marker bit SHALL be
set to zero (M=0).

#### Sources

- [RFC4867](https://tools.ietf.org/html/rfc4867)
