import json
from enum import Enum
from uuid import UUID, uuid4
from dataclasses import dataclass

import pika
from pika.exchange_type import ExchangeType


class BrokerExchangeType(Enum):
    FANOUT: ExchangeType = ExchangeType.fanout
    TOPIC: ExchangeType = ExchangeType.topic


class BrokerConnection:
    _connection: pika.BlockingConnection
    channel: pika.adapters.blocking_connection.BlockingChannel

    def __init__(self, host: str, port: int):
        connection_parameters = pika.ConnectionParameters(
            host=host,
            port=port,
        )
        self._connection = pika.BlockingConnection(parameters=connection_parameters)
        self.channel = self._connection.channel()

    def setup_channel(self, name: str, exchange_type: BrokerExchangeType):
        self.channel.exchange_declare(exchange=name, exchange_type=exchange_type.value)


@dataclass
class BrokerMessage:
    broker_connection: BrokerConnection
    exchange: str
    routing_key: str
    producer: UUID
    body: dict
    identifier: UUID = uuid4()  # Auto generated on initialization

    def send(self) -> None:
        """
        Sends the message to the topic on the message broker.
        Args:

        Returns:
            None
        """
        self.broker_connection.channel.basic_publish(
            exchange=self.exchange,
            routing_key=self.routing_key,
            body=json.dumps(self.body),
        )

    def send_rpc(self, callback_function) -> None:
        """
        Sends a rpc request to on the message broker

        The result will be passed to the passed callback function.
        The result will be a class derived of BaseBrokerReply.
        Args:

        Returns:
            None
        """
        raise NotImplementedError
