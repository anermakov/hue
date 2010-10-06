#
# Autogenerated by Thrift
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#

from thrift.Thrift import *

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None


class TestEnum(object):
  ENUM_ONE = 0
  ENUM_TWO = 1
  ENUM_THREE = 2

  _VALUES_TO_NAMES = {
    0: "ENUM_ONE",
    1: "ENUM_TWO",
    2: "ENUM_THREE",
  }

  _NAMES_TO_VALUES = {
    "ENUM_ONE": 0,
    "ENUM_TWO": 1,
    "ENUM_THREE": 2,
  }


class TestStruct(object):
  """
  Attributes:
   - a
   - b
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRING, 'a', None, None, ), # 1
    (2, TType.I32, 'b', None, None, ), # 2
  )

  def __init__(self, a=None, b=None,):
    self.a = a
    self.b = b

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRING:
          self.a = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.b = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TestStruct')
    if self.a != None:
      oprot.writeFieldBegin('a', TType.STRING, 1)
      oprot.writeString(self.a)
      oprot.writeFieldEnd()
    if self.b != None:
      oprot.writeFieldBegin('b', TType.I32, 2)
      oprot.writeI32(self.b)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TestNesting(object):
  """
  Attributes:
   - nested_struct
   - b
  """

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'nested_struct', (TestStruct, TestStruct.thrift_spec), None, ), # 1
    (2, TType.I32, 'b', None, None, ), # 2
  )

  def __init__(self, nested_struct=None, b=None,):
    self.nested_struct = nested_struct
    self.b = b

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.STRUCT:
          self.nested_struct = TestStruct()
          self.nested_struct.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.b = iprot.readI32();
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TestNesting')
    if self.nested_struct != None:
      oprot.writeFieldBegin('nested_struct', TType.STRUCT, 1)
      self.nested_struct.write(oprot)
      oprot.writeFieldEnd()
    if self.b != None:
      oprot.writeFieldBegin('b', TType.I32, 2)
      oprot.writeI32(self.b)
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)

class TestManyTypes(object):
  """
  Attributes:
   - a_bool
   - a_byte
   - a_i16
   - a_i32
   - a_i64
   - a_double
   - a_string
   - a_binary
   - a_enum
   - a_struct
   - a_set
   - a_list
   - a_map
   - a_string_with_default
   - a_string_list
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'a_bool', None, None, ), # 1
    (2, TType.BYTE, 'a_byte', None, None, ), # 2
    (3, TType.I16, 'a_i16', None, None, ), # 3
    (4, TType.I32, 'a_i32', None, None, ), # 4
    (5, TType.I64, 'a_i64', None, None, ), # 5
    (6, TType.DOUBLE, 'a_double', None, None, ), # 6
    (7, TType.STRING, 'a_string', None, None, ), # 7
    (8, TType.STRING, 'a_binary', None, None, ), # 8
    (9, TType.I32, 'a_enum', None, None, ), # 9
    (10, TType.STRUCT, 'a_struct', (TestStruct, TestStruct.thrift_spec), None, ), # 10
    (11, TType.SET, 'a_set', (TType.I32,None), None, ), # 11
    (12, TType.LIST, 'a_list', (TType.STRUCT,(TestStruct, TestStruct.thrift_spec)), None, ), # 12
    (13, TType.MAP, 'a_map', (TType.I32,None,TType.STRUCT,(TestStruct, TestStruct.thrift_spec)), None, ), # 13
    (14, TType.STRING, 'a_string_with_default', None, "the_default", ), # 14
    (15, TType.LIST, 'a_string_list', (TType.STRING,None), None, ), # 15
  )

  def __init__(self, a_bool=None, a_byte=None, a_i16=None, a_i32=None, a_i64=None, a_double=None, a_string=None, a_binary=None, a_enum=None, a_struct=None, a_set=None, a_list=None, a_map=None, a_string_with_default=thrift_spec[14][4], a_string_list=None,):
    self.a_bool = a_bool
    self.a_byte = a_byte
    self.a_i16 = a_i16
    self.a_i32 = a_i32
    self.a_i64 = a_i64
    self.a_double = a_double
    self.a_string = a_string
    self.a_binary = a_binary
    self.a_enum = a_enum
    self.a_struct = a_struct
    self.a_set = a_set
    self.a_list = a_list
    self.a_map = a_map
    self.a_string_with_default = a_string_with_default
    self.a_string_list = a_string_list

  def read(self, iprot):
    if iprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None and fastbinary is not None:
      fastbinary.decode_binary(self, iprot.trans, (self.__class__, self.thrift_spec))
      return
    iprot.readStructBegin()
    while True:
      (fname, ftype, fid) = iprot.readFieldBegin()
      if ftype == TType.STOP:
        break
      if fid == 1:
        if ftype == TType.BOOL:
          self.a_bool = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.BYTE:
          self.a_byte = iprot.readByte();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I16:
          self.a_i16 = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.I32:
          self.a_i32 = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.I64:
          self.a_i64 = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.DOUBLE:
          self.a_double = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.STRING:
          self.a_string = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.a_binary = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.I32:
          self.a_enum = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 10:
        if ftype == TType.STRUCT:
          self.a_struct = TestStruct()
          self.a_struct.read(iprot)
        else:
          iprot.skip(ftype)
      elif fid == 11:
        if ftype == TType.SET:
          self.a_set = set()
          (_etype3, _size0) = iprot.readSetBegin()
          for _i4 in xrange(_size0):
            _elem5 = iprot.readI32();
            self.a_set.add(_elem5)
          iprot.readSetEnd()
        else:
          iprot.skip(ftype)
      elif fid == 12:
        if ftype == TType.LIST:
          self.a_list = []
          (_etype9, _size6) = iprot.readListBegin()
          for _i10 in xrange(_size6):
            _elem11 = TestStruct()
            _elem11.read(iprot)
            self.a_list.append(_elem11)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 13:
        if ftype == TType.MAP:
          self.a_map = {}
          (_ktype13, _vtype14, _size12 ) = iprot.readMapBegin() 
          for _i16 in xrange(_size12):
            _key17 = iprot.readI32();
            _val18 = TestStruct()
            _val18.read(iprot)
            self.a_map[_key17] = _val18
          iprot.readMapEnd()
        else:
          iprot.skip(ftype)
      elif fid == 14:
        if ftype == TType.STRING:
          self.a_string_with_default = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 15:
        if ftype == TType.LIST:
          self.a_string_list = []
          (_etype22, _size19) = iprot.readListBegin()
          for _i23 in xrange(_size19):
            _elem24 = iprot.readString();
            self.a_string_list.append(_elem24)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      else:
        iprot.skip(ftype)
      iprot.readFieldEnd()
    iprot.readStructEnd()

  def write(self, oprot):
    if oprot.__class__ == TBinaryProtocol.TBinaryProtocolAccelerated and self.thrift_spec is not None and fastbinary is not None:
      oprot.trans.write(fastbinary.encode_binary(self, (self.__class__, self.thrift_spec)))
      return
    oprot.writeStructBegin('TestManyTypes')
    if self.a_bool != None:
      oprot.writeFieldBegin('a_bool', TType.BOOL, 1)
      oprot.writeBool(self.a_bool)
      oprot.writeFieldEnd()
    if self.a_byte != None:
      oprot.writeFieldBegin('a_byte', TType.BYTE, 2)
      oprot.writeByte(self.a_byte)
      oprot.writeFieldEnd()
    if self.a_i16 != None:
      oprot.writeFieldBegin('a_i16', TType.I16, 3)
      oprot.writeI16(self.a_i16)
      oprot.writeFieldEnd()
    if self.a_i32 != None:
      oprot.writeFieldBegin('a_i32', TType.I32, 4)
      oprot.writeI32(self.a_i32)
      oprot.writeFieldEnd()
    if self.a_i64 != None:
      oprot.writeFieldBegin('a_i64', TType.I64, 5)
      oprot.writeI64(self.a_i64)
      oprot.writeFieldEnd()
    if self.a_double != None:
      oprot.writeFieldBegin('a_double', TType.DOUBLE, 6)
      oprot.writeDouble(self.a_double)
      oprot.writeFieldEnd()
    if self.a_string != None:
      oprot.writeFieldBegin('a_string', TType.STRING, 7)
      oprot.writeString(self.a_string)
      oprot.writeFieldEnd()
    if self.a_binary != None:
      oprot.writeFieldBegin('a_binary', TType.STRING, 8)
      oprot.writeString(self.a_binary)
      oprot.writeFieldEnd()
    if self.a_enum != None:
      oprot.writeFieldBegin('a_enum', TType.I32, 9)
      oprot.writeI32(self.a_enum)
      oprot.writeFieldEnd()
    if self.a_struct != None:
      oprot.writeFieldBegin('a_struct', TType.STRUCT, 10)
      self.a_struct.write(oprot)
      oprot.writeFieldEnd()
    if self.a_set != None:
      oprot.writeFieldBegin('a_set', TType.SET, 11)
      oprot.writeSetBegin(TType.I32, len(self.a_set))
      for iter25 in self.a_set:
        oprot.writeI32(iter25)
      oprot.writeSetEnd()
      oprot.writeFieldEnd()
    if self.a_list != None:
      oprot.writeFieldBegin('a_list', TType.LIST, 12)
      oprot.writeListBegin(TType.STRUCT, len(self.a_list))
      for iter26 in self.a_list:
        iter26.write(oprot)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.a_map != None:
      oprot.writeFieldBegin('a_map', TType.MAP, 13)
      oprot.writeMapBegin(TType.I32, TType.STRUCT, len(self.a_map))
      for kiter27,viter28 in self.a_map.items():
        oprot.writeI32(kiter27)
        viter28.write(oprot)
      oprot.writeMapEnd()
      oprot.writeFieldEnd()
    if self.a_string_with_default != None:
      oprot.writeFieldBegin('a_string_with_default', TType.STRING, 14)
      oprot.writeString(self.a_string_with_default)
      oprot.writeFieldEnd()
    if self.a_string_list != None:
      oprot.writeFieldBegin('a_string_list', TType.LIST, 15)
      oprot.writeListBegin(TType.STRING, len(self.a_string_list))
      for iter29 in self.a_string_list:
        oprot.writeString(iter29)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()
    def validate(self):
      return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
