#
# Autogenerated by Thrift Compiler (0.9.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException

from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol, TProtocol
try:
  from thrift.protocol import fastbinary
except:
  fastbinary = None



class TColumnValue:
  """
  Attributes:
   - bool_val
   - byte_val
   - short_val
   - int_val
   - long_val
   - double_val
   - string_val
   - binary_val
   - timestamp_val
  """

  thrift_spec = (
    None, # 0
    (1, TType.BOOL, 'bool_val', None, None, ), # 1
    (2, TType.I32, 'int_val', None, None, ), # 2
    (3, TType.I64, 'long_val', None, None, ), # 3
    (4, TType.DOUBLE, 'double_val', None, None, ), # 4
    (5, TType.STRING, 'string_val', None, None, ), # 5
    (6, TType.BYTE, 'byte_val', None, None, ), # 6
    (7, TType.I16, 'short_val', None, None, ), # 7
    (8, TType.STRING, 'binary_val', None, None, ), # 8
    (9, TType.STRING, 'timestamp_val', None, None, ), # 9
  )

  def __init__(self, bool_val=None, byte_val=None, short_val=None, int_val=None, long_val=None, double_val=None, string_val=None, binary_val=None, timestamp_val=None,):
    self.bool_val = bool_val
    self.byte_val = byte_val
    self.short_val = short_val
    self.int_val = int_val
    self.long_val = long_val
    self.double_val = double_val
    self.string_val = string_val
    self.binary_val = binary_val
    self.timestamp_val = timestamp_val

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
          self.bool_val = iprot.readBool();
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.BYTE:
          self.byte_val = iprot.readByte();
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.I16:
          self.short_val = iprot.readI16();
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.I32:
          self.int_val = iprot.readI32();
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.I64:
          self.long_val = iprot.readI64();
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.DOUBLE:
          self.double_val = iprot.readDouble();
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.STRING:
          self.string_val = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.STRING:
          self.binary_val = iprot.readString();
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.STRING:
          self.timestamp_val = iprot.readString();
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
    oprot.writeStructBegin('TColumnValue')
    if self.bool_val is not None:
      oprot.writeFieldBegin('bool_val', TType.BOOL, 1)
      oprot.writeBool(self.bool_val)
      oprot.writeFieldEnd()
    if self.int_val is not None:
      oprot.writeFieldBegin('int_val', TType.I32, 2)
      oprot.writeI32(self.int_val)
      oprot.writeFieldEnd()
    if self.long_val is not None:
      oprot.writeFieldBegin('long_val', TType.I64, 3)
      oprot.writeI64(self.long_val)
      oprot.writeFieldEnd()
    if self.double_val is not None:
      oprot.writeFieldBegin('double_val', TType.DOUBLE, 4)
      oprot.writeDouble(self.double_val)
      oprot.writeFieldEnd()
    if self.string_val is not None:
      oprot.writeFieldBegin('string_val', TType.STRING, 5)
      oprot.writeString(self.string_val)
      oprot.writeFieldEnd()
    if self.byte_val is not None:
      oprot.writeFieldBegin('byte_val', TType.BYTE, 6)
      oprot.writeByte(self.byte_val)
      oprot.writeFieldEnd()
    if self.short_val is not None:
      oprot.writeFieldBegin('short_val', TType.I16, 7)
      oprot.writeI16(self.short_val)
      oprot.writeFieldEnd()
    if self.binary_val is not None:
      oprot.writeFieldBegin('binary_val', TType.STRING, 8)
      oprot.writeString(self.binary_val)
      oprot.writeFieldEnd()
    if self.timestamp_val is not None:
      oprot.writeFieldBegin('timestamp_val', TType.STRING, 9)
      oprot.writeString(self.timestamp_val)
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

class TResultRow:
  """
  Attributes:
   - colVals
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'colVals', (TType.STRUCT,(TColumnValue, TColumnValue.thrift_spec)), None, ), # 1
  )

  def __init__(self, colVals=None,):
    self.colVals = colVals

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
        if ftype == TType.LIST:
          self.colVals = []
          (_etype3, _size0) = iprot.readListBegin()
          for _i4 in xrange(_size0):
            _elem5 = TColumnValue()
            _elem5.read(iprot)
            self.colVals.append(_elem5)
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
    oprot.writeStructBegin('TResultRow')
    if self.colVals is not None:
      oprot.writeFieldBegin('colVals', TType.LIST, 1)
      oprot.writeListBegin(TType.STRUCT, len(self.colVals))
      for iter6 in self.colVals:
        iter6.write(oprot)
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

class TColumnData:
  """
  Attributes:
   - is_null
   - bool_vals
   - byte_vals
   - short_vals
   - int_vals
   - long_vals
   - double_vals
   - string_vals
   - binary_vals
  """

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'is_null', (TType.BOOL,None), None, ), # 1
    (2, TType.LIST, 'bool_vals', (TType.BOOL,None), None, ), # 2
    (3, TType.LIST, 'byte_vals', (TType.BYTE,None), None, ), # 3
    (4, TType.LIST, 'short_vals', (TType.I16,None), None, ), # 4
    (5, TType.LIST, 'int_vals', (TType.I32,None), None, ), # 5
    (6, TType.LIST, 'long_vals', (TType.I64,None), None, ), # 6
    (7, TType.LIST, 'double_vals', (TType.DOUBLE,None), None, ), # 7
    (8, TType.LIST, 'string_vals', (TType.STRING,None), None, ), # 8
    (9, TType.LIST, 'binary_vals', (TType.STRING,None), None, ), # 9
  )

  def __init__(self, is_null=None, bool_vals=None, byte_vals=None, short_vals=None, int_vals=None, long_vals=None, double_vals=None, string_vals=None, binary_vals=None,):
    self.is_null = is_null
    self.bool_vals = bool_vals
    self.byte_vals = byte_vals
    self.short_vals = short_vals
    self.int_vals = int_vals
    self.long_vals = long_vals
    self.double_vals = double_vals
    self.string_vals = string_vals
    self.binary_vals = binary_vals

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
        if ftype == TType.LIST:
          self.is_null = []
          (_etype10, _size7) = iprot.readListBegin()
          for _i11 in xrange(_size7):
            _elem12 = iprot.readBool();
            self.is_null.append(_elem12)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 2:
        if ftype == TType.LIST:
          self.bool_vals = []
          (_etype16, _size13) = iprot.readListBegin()
          for _i17 in xrange(_size13):
            _elem18 = iprot.readBool();
            self.bool_vals.append(_elem18)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 3:
        if ftype == TType.LIST:
          self.byte_vals = []
          (_etype22, _size19) = iprot.readListBegin()
          for _i23 in xrange(_size19):
            _elem24 = iprot.readByte();
            self.byte_vals.append(_elem24)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 4:
        if ftype == TType.LIST:
          self.short_vals = []
          (_etype28, _size25) = iprot.readListBegin()
          for _i29 in xrange(_size25):
            _elem30 = iprot.readI16();
            self.short_vals.append(_elem30)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 5:
        if ftype == TType.LIST:
          self.int_vals = []
          (_etype34, _size31) = iprot.readListBegin()
          for _i35 in xrange(_size31):
            _elem36 = iprot.readI32();
            self.int_vals.append(_elem36)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 6:
        if ftype == TType.LIST:
          self.long_vals = []
          (_etype40, _size37) = iprot.readListBegin()
          for _i41 in xrange(_size37):
            _elem42 = iprot.readI64();
            self.long_vals.append(_elem42)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 7:
        if ftype == TType.LIST:
          self.double_vals = []
          (_etype46, _size43) = iprot.readListBegin()
          for _i47 in xrange(_size43):
            _elem48 = iprot.readDouble();
            self.double_vals.append(_elem48)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 8:
        if ftype == TType.LIST:
          self.string_vals = []
          (_etype52, _size49) = iprot.readListBegin()
          for _i53 in xrange(_size49):
            _elem54 = iprot.readString();
            self.string_vals.append(_elem54)
          iprot.readListEnd()
        else:
          iprot.skip(ftype)
      elif fid == 9:
        if ftype == TType.LIST:
          self.binary_vals = []
          (_etype58, _size55) = iprot.readListBegin()
          for _i59 in xrange(_size55):
            _elem60 = iprot.readString();
            self.binary_vals.append(_elem60)
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
    oprot.writeStructBegin('TColumnData')
    if self.is_null is not None:
      oprot.writeFieldBegin('is_null', TType.LIST, 1)
      oprot.writeListBegin(TType.BOOL, len(self.is_null))
      for iter61 in self.is_null:
        oprot.writeBool(iter61)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.bool_vals is not None:
      oprot.writeFieldBegin('bool_vals', TType.LIST, 2)
      oprot.writeListBegin(TType.BOOL, len(self.bool_vals))
      for iter62 in self.bool_vals:
        oprot.writeBool(iter62)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.byte_vals is not None:
      oprot.writeFieldBegin('byte_vals', TType.LIST, 3)
      oprot.writeListBegin(TType.BYTE, len(self.byte_vals))
      for iter63 in self.byte_vals:
        oprot.writeByte(iter63)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.short_vals is not None:
      oprot.writeFieldBegin('short_vals', TType.LIST, 4)
      oprot.writeListBegin(TType.I16, len(self.short_vals))
      for iter64 in self.short_vals:
        oprot.writeI16(iter64)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.int_vals is not None:
      oprot.writeFieldBegin('int_vals', TType.LIST, 5)
      oprot.writeListBegin(TType.I32, len(self.int_vals))
      for iter65 in self.int_vals:
        oprot.writeI32(iter65)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.long_vals is not None:
      oprot.writeFieldBegin('long_vals', TType.LIST, 6)
      oprot.writeListBegin(TType.I64, len(self.long_vals))
      for iter66 in self.long_vals:
        oprot.writeI64(iter66)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.double_vals is not None:
      oprot.writeFieldBegin('double_vals', TType.LIST, 7)
      oprot.writeListBegin(TType.DOUBLE, len(self.double_vals))
      for iter67 in self.double_vals:
        oprot.writeDouble(iter67)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.string_vals is not None:
      oprot.writeFieldBegin('string_vals', TType.LIST, 8)
      oprot.writeListBegin(TType.STRING, len(self.string_vals))
      for iter68 in self.string_vals:
        oprot.writeString(iter68)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    if self.binary_vals is not None:
      oprot.writeFieldBegin('binary_vals', TType.LIST, 9)
      oprot.writeListBegin(TType.STRING, len(self.binary_vals))
      for iter69 in self.binary_vals:
        oprot.writeString(iter69)
      oprot.writeListEnd()
      oprot.writeFieldEnd()
    oprot.writeFieldStop()
    oprot.writeStructEnd()

  def validate(self):
    if self.is_null is None:
      raise TProtocol.TProtocolException(message='Required field is_null is unset!')
    return


  def __repr__(self):
    L = ['%s=%r' % (key, value)
      for key, value in self.__dict__.iteritems()]
    return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

  def __eq__(self, other):
    return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

  def __ne__(self, other):
    return not (self == other)
