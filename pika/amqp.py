"""amqp.py

Auto-generated AMQP Support Module

WARNING: DO NOT EDIT. To Generate run tools/codegen.py

For copyright and licensing please refer to COPYING.

"""

__date__ = "2011-04-11"
__author__ = "codegen.py"

# AMQP Protocol Version
AMQP_VERSION = (0, 9, 1)

# RabbitMQ Defaults
DEFAULT_HOST = "localhost"
DEFAULT_PORT = 5672
DEFAULT_USER = "guest"
DEFAULT_PASS = "guest"

# AMQP Constants
AMQP_FRAME_METHOD = 1
AMQP_FRAME_HEADER = 2
AMQP_FRAME_BODY = 3
AMQP_FRAME_HEARTBEAT = 8
AMQP_FRAME_MIN_SIZE = 4096
AMQP_FRAME_END = 206
AMQP_REPLY_SUCCESS = 200

# AMQP data types
AMQP_DATA_TYPES = ["bit",
                   "long",
                   "longlong",
                   "longstr",
                   "octet",
                   "short",
                   "shortstr",
                   "table",
                   "timestamp"]

# AMQP domains
AMQP_DOMAINS = {"channel-id": "longstr",
                "class-id": "short",
                "consumer-tag": "shortstr",
                "delivery-tag": "longlong",
                "destination": "shortstr",
                "duration": "longlong",
                "exchange-name": "shortstr",
                "method-id": "short",
                "no-ack": "bit",
                "no-local": "bit",
                "offset": "longlong",
                "path": "shortstr",
                "peer-properties": "table",
                "queue-name": "shortstr",
                "redelivered": "bit",
                "reference": "longstr",
                "reject-code": "short",
                "reject-text": "shortstr",
                "reply-code": "short",
                "reply-text": "shortstr",
                "security-token": "longstr"}


# AMQP Errors
class AMQPContentTooLarge(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "CONTENT-TOO-LARGE"
    value = 311


class AMQPNoRoute(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "NO-ROUTE"
    value = 312


class AMQPNoConsumers(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "NO-CONSUMERS"
    value = 313


class AMQPAccessRefused(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "ACCESS-REFUSED"
    value = 403


class AMQPNotFound(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "NOT-FOUND"
    value = 404


class AMQPResourceLocked(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "RESOURCE-LOCKED"
    value = 405


class AMQPPreconditionFailed(Warning):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "PRECONDITION-FAILED"
    value = 406


class AMQPConnectionForced(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "CONNECTION-FORCED"
    value = 320


class AMQPInvalidPath(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "INVALID-PATH"
    value = 402


class AMQPFrameError(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "FRAME-ERROR"
    value = 501


class AMQPSyntaxError(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "SYNTAX-ERROR"
    value = 502


class AMQPCommandInvalid(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "COMMAND-INVALID"
    value = 503


class AMQPChannelError(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "CHANNEL-ERROR"
    value = 504


class AMQPUnexpectedFrame(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "UNEXPECTED-FRAME"
    value = 505


class AMQPResourceError(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "RESOURCE-ERROR"
    value = 506


class AMQPNotAllowed(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "NOT-ALLOWED"
    value = 530


class AMQPNotImplemented(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "NOT-IMPLEMENTED"
    value = 540


class AMQPInternalError(Exception):
    """Class used to map AMQP error values to an Exception
    or Warning class based upon being a hard or soft error.

    """
    name = "INTERNAL-ERROR"
    value = 541


# AMQP class to id mapping
AMQP_CLASSES = {"CONNECTION": 10,
                "CHANNEL": 20,
                "ACCESS": 30,
                "EXCHANGE": 40,
                "QUEUE": 50,
                "BASIC": 60,
                "TX": 90,
                "CONFIRM": 85}

# AMQP Error code to class mapping
AMQP_ERRORS = {320: AMQPConnectionForced,
               505: AMQPUnexpectedFrame,
               502: AMQPSyntaxError,
               503: AMQPCommandInvalid,
               530: AMQPNotAllowed,
               504: AMQPChannelError,
               402: AMQPInvalidPath,
               403: AMQPAccessRefused,
               404: AMQPNotFound,
               405: AMQPResourceLocked,
               406: AMQPPreconditionFailed,
               311: AMQPContentTooLarge,
               312: AMQPNoRoute,
               313: AMQPNoConsumers,
               506: AMQPResourceError,
               540: AMQPNotImplemented,
               541: AMQPInternalError,
               501: AMQPFrameError}

# AMQP Classes and Methods
FRAMES = {60:{"name": "basic",
              "methods": {10: {"name": "qos",
                               "args": [{"name": "prefetch-size",
                                        "type": "long",
                                        "default": 0},
                                        {"name": "prefetch-count",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "global",
                                        "type": "bit",
                                        "default": 0}],
                               "synchronous": True},
                          11: {"name": "qos-ok",
                               "synchronous": False},
                          20: {"name": "consume",
                               "args": [{"name": "ticket",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "queue",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "consumer-tag",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "no-local",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "no-ack",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "exclusive",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "nowait",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "arguments",
                                        "type": "table",
                                        "default": None}],
                               "synchronous": True},
                          21: {"name": "consume-ok",
                               "args": [{"name": "consumer-tag",
                                        "type": "shortstr",
                                        "default": None}],
                               "synchronous": False},
                          30: {"name": "cancel",
                               "args": [{"name": "consumer-tag",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "nowait",
                                        "type": "bit",
                                        "default": 0}],
                               "synchronous": True},
                          31: {"name": "cancel-ok",
                               "args": [{"name": "consumer-tag",
                                        "type": "shortstr",
                                        "default": None}],
                               "synchronous": False},
                          40: {"name": "publish",
                               "args": [{"name": "ticket",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "exchange",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "routing-key",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "mandatory",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "immediate",
                                        "type": "bit",
                                        "default": 0}],
                               "synchronous": False},
                          50: {"name": "return",
                               "args": [{"name": "reply-code",
                                        "type": "short",
                                        "default": None},
                                        {"name": "reply-text",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "exchange",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "routing-key",
                                        "type": "shortstr",
                                        "default": None}],
                               "synchronous": False},
                          60: {"name": "deliver",
                               "args": [{"name": "consumer-tag",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "delivery-tag",
                                        "type": "longlong",
                                        "default": None},
                                        {"name": "redelivered",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "exchange",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "routing-key",
                                        "type": "shortstr",
                                        "default": None}],
                               "synchronous": False},
                          70: {"name": "get",
                               "args": [{"name": "ticket",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "queue",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "no-ack",
                                        "type": "bit",
                                        "default": 0}],
                               "synchronous": True},
                          71: {"name": "get-ok",
                               "args": [{"name": "delivery-tag",
                                        "type": "longlong",
                                        "default": None},
                                        {"name": "redelivered",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "exchange",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "routing-key",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "message-count",
                                        "type": "long",
                                        "default": None}],
                               "synchronous": False},
                          72: {"name": "get-empty",
                               "args": [{"name": "cluster-id",
                                        "type": "shortstr",
                                        "default": None}],
                               "synchronous": False},
                          80: {"name": "ack",
                               "args": [{"name": "delivery-tag",
                                        "type": "longlong",
                                        "default": 0},
                                        {"name": "multiple",
                                        "type": "bit",
                                        "default": 0}],
                               "synchronous": False},
                          90: {"name": "reject",
                               "args": [{"name": "delivery-tag",
                                        "type": "longlong",
                                        "default": None},
                                        {"name": "requeue",
                                        "type": "bit",
                                        "default": 1}],
                               "synchronous": False},
                          100: {"name": "recover-async",
                                "args": [{"name": "requeue",
                                         "type": "bit",
                                         "default": 0}],
                                "synchronous": False},
                          110: {"name": "recover",
                                "args": [{"name": "requeue",
                                         "type": "bit",
                                         "default": 0}],
                                "synchronous": True},
                          111: {"name": "recover-ok",
                                "synchronous": False},
                          120: {"name": "nack",
                                "args": [{"name": "delivery-tag",
                                         "type": "longlong",
                                         "default": 0},
                                         {"name": "multiple",
                                         "type": "bit",
                                         "default": 0},
                                         {"name": "requeue",
                                         "type": "bit",
                                         "default": 1}],
                                "synchronous": False}},
              "properties": [{"name": "content-type",
                              "type": "shortstr",
                              "default": None},
                             {"name": "content-encoding",
                              "type": "shortstr",
                              "default": None},
                             {"name": "headers",
                              "type": "table",
                              "default": None},
                             {"name": "delivery-mode",
                              "type": "octet",
                              "default": None},
                             {"name": "priority",
                              "type": "octet",
                              "default": None},
                             {"name": "correlation-id",
                              "type": "shortstr",
                              "default": None},
                             {"name": "reply-to",
                              "type": "shortstr",
                              "default": None},
                             {"name": "expiration",
                              "type": "shortstr",
                              "default": None},
                             {"name": "message-id",
                              "type": "shortstr",
                              "default": None},
                             {"name": "timestamp",
                              "type": "timestamp",
                              "default": None},
                             {"name": "type",
                              "type": "shortstr",
                              "default": None},
                             {"name": "user-id",
                              "type": "shortstr",
                              "default": None},
                             {"name": "app-id",
                              "type": "shortstr",
                              "default": None},
                             {"name": "cluster-id",
                              "type": "shortstr",
                              "default": None}]},
          20:{"name": "channel",
              "methods": {10: {"name": "open",
                               "args": [{"name": "out-of-band",
                                        "type": "shortstr",
                                        "default": None}],
                               "synchronous": True},
                          11: {"name": "open-ok",
                               "args": [{"name": "channel-id",
                                        "type": "longstr",
                                        "default": None}],
                               "synchronous": False},
                          20: {"name": "flow",
                               "args": [{"name": "active",
                                        "type": "bit",
                                        "default": None}],
                               "synchronous": True},
                          21: {"name": "flow-ok",
                               "args": [{"name": "active",
                                        "type": "bit",
                                        "default": None}],
                               "synchronous": False},
                          40: {"name": "close",
                               "args": [{"name": "reply-code",
                                        "type": "short",
                                        "default": None},
                                        {"name": "reply-text",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "class-id",
                                        "type": "short",
                                        "default": None},
                                        {"name": "method-id",
                                        "type": "short",
                                        "default": None}],
                               "synchronous": True},
                          41: {"name": "close-ok",
                               "synchronous": False}}},
          85:{"name": "confirm",
              "methods": {10: {"name": "select",
                               "args": [{"name": "nowait",
                                        "type": "bit",
                                        "default": 0}],
                               "synchronous": True},
                          11: {"name": "select-ok",
                               "synchronous": False}}},
          10:{"name": "connection",
              "methods": {10: {"name": "start",
                               "args": [{"name": "version-major",
                                        "type": "octet",
                                        "default": 0},
                                        {"name": "version-minor",
                                        "type": "octet",
                                        "default": 9},
                                        {"name": "server-properties",
                                        "type": "table",
                                        "default": None},
                                        {"name": "mechanisms",
                                        "type": "longstr",
                                        "default": "PLAIN"},
                                        {"name": "locales",
                                        "type": "longstr",
                                        "default": "en_US"}],
                               "synchronous": True},
                          11: {"name": "start-ok",
                               "args": [{"name": "client-properties",
                                        "type": "table",
                                        "default": None},
                                        {"name": "mechanism",
                                        "type": "shortstr",
                                        "default": "PLAIN"},
                                        {"name": "response",
                                        "type": "longstr",
                                        "default": None},
                                        {"name": "locale",
                                        "type": "shortstr",
                                        "default": "en_US"}],
                               "synchronous": False},
                          20: {"name": "secure",
                               "args": [{"name": "challenge",
                                        "type": "longstr",
                                        "default": None}],
                               "synchronous": True},
                          21: {"name": "secure-ok",
                               "args": [{"name": "response",
                                        "type": "longstr",
                                        "default": None}],
                               "synchronous": False},
                          30: {"name": "tune",
                               "args": [{"name": "channel-max",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "frame-max",
                                        "type": "long",
                                        "default": 0},
                                        {"name": "heartbeat",
                                        "type": "short",
                                        "default": 0}],
                               "synchronous": True},
                          31: {"name": "tune-ok",
                               "args": [{"name": "channel-max",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "frame-max",
                                        "type": "long",
                                        "default": 0},
                                        {"name": "heartbeat",
                                        "type": "short",
                                        "default": 0}],
                               "synchronous": False},
                          40: {"name": "open",
                               "args": [{"name": "virtual-host",
                                        "type": "shortstr",
                                        "default": "/"},
                                        {"name": "capabilities",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "insist",
                                        "type": "bit",
                                        "default": 0}],
                               "synchronous": True},
                          41: {"name": "open-ok",
                               "args": [{"name": "known-hosts",
                                        "type": "shortstr",
                                        "default": None}],
                               "synchronous": False},
                          50: {"name": "close",
                               "args": [{"name": "reply-code",
                                        "type": "short",
                                        "default": None},
                                        {"name": "reply-text",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "class-id",
                                        "type": "short",
                                        "default": None},
                                        {"name": "method-id",
                                        "type": "short",
                                        "default": None}],
                               "synchronous": True},
                          51: {"name": "close-ok",
                               "synchronous": False}}},
          40:{"name": "exchange",
              "methods": {10: {"name": "declare",
                               "args": [{"name": "ticket",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "exchange",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "type",
                                        "type": "shortstr",
                                        "default": "direct"},
                                        {"name": "passive",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "durable",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "auto-delete",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "internal",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "nowait",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "arguments",
                                        "type": "table",
                                        "default": None}],
                               "synchronous": True},
                          11: {"name": "declare-ok",
                               "synchronous": False},
                          20: {"name": "delete",
                               "args": [{"name": "ticket",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "exchange",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "if-unused",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "nowait",
                                        "type": "bit",
                                        "default": 0}],
                               "synchronous": True},
                          21: {"name": "delete-ok",
                               "synchronous": False},
                          30: {"name": "bind",
                               "args": [{"name": "ticket",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "destination",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "source",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "routing-key",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "nowait",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "arguments",
                                        "type": "table",
                                        "default": None}],
                               "synchronous": True},
                          31: {"name": "bind-ok",
                               "synchronous": False},
                          40: {"name": "unbind",
                               "args": [{"name": "ticket",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "destination",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "source",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "routing-key",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "nowait",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "arguments",
                                        "type": "table",
                                        "default": None}],
                               "synchronous": True},
                          51: {"name": "unbind-ok",
                               "synchronous": False}}},
          50:{"name": "queue",
              "methods": {10: {"name": "declare",
                               "args": [{"name": "ticket",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "queue",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "passive",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "durable",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "exclusive",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "auto-delete",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "nowait",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "arguments",
                                        "type": "table",
                                        "default": None}],
                               "synchronous": True},
                          11: {"name": "declare-ok",
                               "args": [{"name": "queue",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "message-count",
                                        "type": "long",
                                        "default": None},
                                        {"name": "consumer-count",
                                        "type": "long",
                                        "default": None}],
                               "synchronous": False},
                          20: {"name": "bind",
                               "args": [{"name": "ticket",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "queue",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "exchange",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "routing-key",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "nowait",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "arguments",
                                        "type": "table",
                                        "default": None}],
                               "synchronous": True},
                          21: {"name": "bind-ok",
                               "synchronous": False},
                          30: {"name": "purge",
                               "args": [{"name": "ticket",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "queue",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "nowait",
                                        "type": "bit",
                                        "default": 0}],
                               "synchronous": True},
                          31: {"name": "purge-ok",
                               "args": [{"name": "message-count",
                                        "type": "long",
                                        "default": None}],
                               "synchronous": False},
                          40: {"name": "delete",
                               "args": [{"name": "ticket",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "queue",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "if-unused",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "if-empty",
                                        "type": "bit",
                                        "default": 0},
                                        {"name": "nowait",
                                        "type": "bit",
                                        "default": 0}],
                               "synchronous": True},
                          41: {"name": "delete-ok",
                               "args": [{"name": "message-count",
                                        "type": "long",
                                        "default": None}],
                               "synchronous": False},
                          50: {"name": "unbind",
                               "args": [{"name": "ticket",
                                        "type": "short",
                                        "default": 0},
                                        {"name": "queue",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "exchange",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "routing-key",
                                        "type": "shortstr",
                                        "default": None},
                                        {"name": "arguments",
                                        "type": "table",
                                        "default": None}],
                               "synchronous": True},
                          51: {"name": "unbind-ok",
                               "synchronous": False}}},
          90:{"name": "tx",
              "methods": {10: {"name": "select",
                               "synchronous": True},
                          11: {"name": "select-ok",
                               "synchronous": False},
                          20: {"name": "commit",
                               "synchronous": True},
                          21: {"name": "commit-ok",
                               "synchronous": False},
                          30: {"name": "rollback",
                               "synchronous": True},
                          31: {"name": "rollback-ok",
                               "synchronous": False}}}}
