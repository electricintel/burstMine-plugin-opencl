/*
	Burst mine
	Distributed graphical plotter and miner for Burst.
	Author: Cryo
	Bitcoin: 138gMBhCrNkbaiTCmUhP9HLU9xwn5QKZgD
	Burst: BURST-YA29-QCEW-QXC3-BKXDL
*/

return $q.all([
	context.addPluginScript('opencl', 'burstMine-plugin-opencl-generator-opencl-edit.js'),
	context.addPluginScript('opencl', 'burstMine-plugin-opencl-generator-opencl-view.js'),
	context.addPluginScript('opencl', 'burstMine-plugin-opencl-platform-view.js'),
	context.addPluginScript('opencl', 'burstMine-plugin-opencl-device-view.js')
]);