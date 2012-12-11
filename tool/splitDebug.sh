#!/bin/bash
for((i=1;i<100;i++));do cat debugfile.log | grep Thread-$i >> Thread-$i.log; done
