#!/bin/bash
# Disable VAAPI hardware decoding (causes GStreamer qtdemux errors in pdfpc)
export LIBVA_DRIVER_NAME=null

pdfpc main.pdf "$@"
