from sqlalchemy import Numeric
import sqlalchemy.types as types


class UnaryValueObjectType(types.TypeDecorator):
    impl = Numeric

    def __init__(self, class_of_value_object, type):
        self.class_of_value_object = class_of_value_object
        self.type = type
        super(UnaryValueObjectType, self).__init__()

    def load_dialect_impl(self, dialect):
        return dialect.type_descriptor(self.type)

    def process_bind_param(self, value_object, dialect):
        if isinstance(value_object, self.class_of_value_object) and value_object is not None:
            value = value_object.value
        return value

    def process_result_value(self, value, dialect):
        if value is not None:
            value_object = self.class_of_value_object(value)
        return value_object