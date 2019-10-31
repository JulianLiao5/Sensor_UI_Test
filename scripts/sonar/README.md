sonar_check_framerate.py
    function: 查看sonar时间间隔/帧率的工具
    输入：sonar的raw data，比如：raw_sonars_data_20190906_164528.txt
    输出：0x790 / 0x791 的两帧之间的时间间隔

sonar_check_framerate_Range.py
    function: 如果是1带2的超声，将65535数据过滤后，8个探头画在一张图里

sonar_RANGE_compare_origin_filtered.py
    function: 针对1带2超声，比较8个探头原始数据和将65535滤掉后的数据，ID0/1/2/3 4个探头画在一张表里，ID4/5/6/7 4个探头画在另一张表里。
