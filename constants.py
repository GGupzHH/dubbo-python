# -*- coding: UTF-8 -*-
# @Create   : 2022/7/5 16:09
# @Author   : yh
# @Remark   :

from .util import num_2_byte_list

# 服务端的响应码
response_status_message = {
    20: 'OK',
    30: 'CLIENT_TIMEOUT',
    31: 'SERVER_TIMEOUT',
    40: 'BAD_REQUEST',
    50: 'BAD_RESPONSE',
    60: 'SERVICE_NOT_FOUND',
    70: 'SERVICE_ERROR',
    80: 'SERVER_ERROR',
    90: 'CLIENT_ERROR'
}

# 32位整型的最大值
MAX_INT_32 = 2147483647
# 32位整型的最小值
MIN_INT_32 = -2147483648

# MAGIC_NUM(2) + FLAG(1) + STATUS(1)
DEFAULT_REQUEST_META = num_2_byte_list(0xdabbc200)

# 客户端对服务端发送的心跳的请求的头部
CLI_HEARTBEAT_REQ_HEAD = num_2_byte_list(0xdabbe2) + [0]
# 客户端对服务端发送的心跳的响应的头部
CLI_HEARTBEAT_RES_HEAD = num_2_byte_list(0xdabb2214)
# 心跳尾部
CLI_HEARTBEAT_TAIL = [0, 0, 0, 1] + num_2_byte_list(0x4e)

DUBBO_ZK_PROVIDERS = '/dubbo/{}/providers'
DUBBO_ZK_CONSUMERS = '/dubbo/{}/consumers'
DUBBO_ZK_CONFIGURATORS = '/dubbo/{}/configurators'

DUBBO_NC_PROVIDERS = 'providers:{}:{}'
DUBBO_NC_CONSUMERS = 'consumers:{}:{}'
# 客户端检测与远程主机的连接是否超时的间隔
TIMEOUT_CHECK_INTERVAL = 0.03  # 30ms
# 连接最长允许的空闲时间
TIMEOUT_IDLE = 60
# 连接允许的最多的超时次数
TIMEOUT_MAX_TIMES = 3
# 每个host允许的最大连接数量
CONN_MAX = 5

# 默认每次读取长度
DEFAULT_READ_PARAMS = 1500

INIT_THREAD = True
