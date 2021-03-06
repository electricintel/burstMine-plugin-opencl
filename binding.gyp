{
	"targets":[
		{
			"target_name":"burstMine-plugin-opencl",
			"sources":[
				"../../../src/burstMine/ScoopsBuffer.cpp",
				"../../../src/burstMine/Generator.cpp",
				"../../../src/burstMine/GenerationWork.cpp",
				"../../../src/burstMine/js/JsScoopsBuffer.cpp",
				"../../../src/burstMine/js/JsGenerationWork.cpp",
				"../../../src/burstMine/js/impl/AsyncData.cpp",
				"src/opencl/OpenclError.cpp",
				"src/opencl/OpenclPlatform.cpp",
				"src/opencl/OpenclDevice.cpp",
				"src/opencl/OpenclContext.cpp",
				"src/opencl/OpenclCommandQueue.cpp",
				"src/opencl/OpenclBuffer.cpp",
				"src/opencl/OpenclProgram.cpp",
				"src/opencl/OpenclKernel.cpp",
				"src/opencl/js/JsOpenclError.cpp",
				"src/opencl/js/JsOpenclPlatform.cpp",
				"src/opencl/js/JsOpenclDevice.cpp",
				"src/burstMine/plugins/opencl/GeneratorOpencl.cpp",
				"src/burstMine/plugins/opencl/GeneratorOpenclConfig.cpp",
				"src/burstMine/plugins/opencl/js/JsGeneratorOpencl.cpp",
				"src/burstMine/plugins/opencl/js/JsGeneratorOpenclConfig.cpp",
				"src/burstMine/plugins/opencl/js/JsPluginOpencl.cpp",
				"src/burstMine/plugins/opencl/js/impl/AsyncDataOpencl.cpp"
			],
			"conditions":[
				["OS == 'win'", {
					"variables":{
						"opencl_include_path%":"<!(IF DEFINED OPENCL_INCLUDE_PATH (echo %OPENCL_INCLUDE_PATH%) ELSE (echo deps/opencl/include))",
						"opencl_lib_path%":"<!(IF DEFINED OPENCL_LIB_PATH (echo %OPENCL_LIB_PATH%) ELSE (echo deps/opencl/lib/win/<(target_arch)))"
					},
					"configurations":{
						"Release":{
							"msvs_settings":{
								"VCCLCompilerTool":{
									"ExceptionHandling":1,
									"DisableSpecificWarnings":["4290"]
								}
							}
						}
					},
					"link_settings":{
						"library_dirs":[
							"<(opencl_lib_path)"
						],
						"libraries":[
							"-lOpenCL"
						]
					}
				}]
			],
			"include_dirs":[
				"<(opencl_include_path)",
				"../../../src"
			]
		},
		{
			"target_name":"post-build",
			"type":"none",
			"dependencies":["burstMine-plugin-opencl"],
			"copies":[
				{
					"files":["<(PRODUCT_DIR)/burstMine-plugin-opencl.node"],
					"destination":"bin"
				}
			]
		}
	]
}