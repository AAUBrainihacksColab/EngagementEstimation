# Useful constants used by the Vision modules.

# Camera model
kOV7670  = 1 # VGA camera
kMT9M114 = 2 # HD wide angle camera
kOV5640 = 3 # New HD camera
kXTION = 4
kSimulator2D = 5
kSimulator3D = 6
kStereo = 7
kOV4689 = 8

# Camera index
kTopCamera = 0
kBottomCamera = 1
kDepthCamera = 2
kStereoCamera = 3

# Image format
k16VGA  = 4 # 2560*1920
k4VGA   = 3 # 1280*960
kVGA    = 2 # 640*480
kQVGA   = 1 # 320*240
kQQVGA  = 0 # 160*120
kQQQVGA = 7 # 80*60
kQQQQVGA = 8 # 40*30

k1080p  = 6 # 1920*1080
k720p   = 5 # 1280*720
kQ720p   = 9 # 640*360
kQQ720p   = 10 # 320*180
kQQQ720p   = 11 # 160*90
kQQQQ720p   = 12 # 80*45

k720px2   = 13 # 2560*720
kQ720px2   = 14 # 1280*360
kQQ720px2   = 15 # 640*180
kQQQ720px2   = 16 # 320*90
kQQQQ720px2   = 17 # 160*45

k960p   = k4VGA # deprecated
k1920p  = k16VGA # deprecated

# Color Space
kYuvColorSpace = 0
kyUvColorSpace = 1
kyuVColorSpace = 2
kRgbColorSpace = 3
krGbColorSpace = 4
krgBColorSpace = 5
kHsvColorSpace = 6
khSvColorSpace = 7
khsVColorSpace = 8
kYUV422ColorSpace = 9
kYUV422InterlacedColorSpace = 9  #deprecated
kYUVColorSpace = 10
kRGBColorSpace = 11
kHSVColorSpace = 12
kBGRColorSpace = 13
kYYCbCrColorSpace = 14
kH2RGBColorSpace = 15
kHSMixedColorSpace = 16
kDepthColorSpace = 17
kARGBColorSpace = 18
kXYZColorSpace = 19
kInfraredColorSpace = 20
kDistanceColorSpace = 21
kLabColorSpace = 22
kRawDepthColorSpace = 23
kLuvColorSpace = 24
kLChabColorSpace = 25
kLChuvColorSpace = 26

# Scale methods
kSimpleScaleMethod = 0
kAverageScaleMethod = 1
kQualityScaleMethod = 2
kNoScaling = 3

# Standard Camera Parameter Id
kCameraBrightnessID       = 0
kCameraContrastID         = 1
kCameraSaturationID       = 2
kCameraHueID              = 3
kCameraRedChromaID        = 4
kCameraBlueChromaID       = 5
kCameraGainID             = 6
kCameraHFlipID            = 7
kCameraVFlipID            = 8
kCameraLensXID            = 9
kCameraLensYID            = 10
kCameraAutoExpositionID   = 11
kCameraAutoWhiteBalanceID = 12
kCameraAutoGainID         = 13
kCameraResolutionID       = 14
kCameraFrameRateID        = 15
kCameraBufferSizeID       = 16
kCameraExposureID         = 17
kCameraSelectID           = 18
kCameraSetDefaultParamsID = 19
kCameraColorSpaceID       = 20
kCameraExposureCorrectionID = 21
kCameraExposureAlgorithmID  = 22
kCameraAecAlgorithmID     = kCameraExposureAlgorithmID
kCameraFastSwitchID       = 23
kCameraSharpnessID        = 24
kCameraAwbGreenGainID     = 25
kCameraAblcID             = 26
kCameraAblcTargetID       = 27
kCameraAblcStableRangeID  = 28
kCameraBlcBlueID          = 29
kCameraBlcRedID           = 30
kCameraBlcGbID            = 31
kCameraBlcGrID            = 32
kCameraWhiteBalanceID     = 33
kCameraBacklightCompensationID = 34
kCameraKeepAliveID        = 35
kCameraDepthConfidenceThresholdID = 36
kCameraDepthFastFilterID  = 37
kCameraTemperatureID      = 38
kCameraAverageLuminanceID = 39
kCameraAutoFocusID        = 40
kCameraSynchronisationID  = 41
kCameraDisparityWindowSizeID = 42
kCameraFocusID = 43
kCameraTestPatternID = 44
