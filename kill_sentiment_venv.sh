#!/usr/bin/env bash

VENVNAME=sentiment
jupyter kernelspec uninstall $VENVNAME
rm -r $VENVNAME