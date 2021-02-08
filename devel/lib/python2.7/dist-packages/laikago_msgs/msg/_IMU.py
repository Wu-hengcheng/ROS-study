# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from laikago_msgs/IMU.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class IMU(genpy.Message):
  _md5sum = "6067de14374c97a8666801686a8446fb"
  _type = "laikago_msgs/IMU"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """float32[4] quaternion
float32[3] gyroscope
float32[3] acceleration
float32[3] rpy
float32 temp"""
  __slots__ = ['quaternion','gyroscope','acceleration','rpy','temp']
  _slot_types = ['float32[4]','float32[3]','float32[3]','float32[3]','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       quaternion,gyroscope,acceleration,rpy,temp

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(IMU, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.quaternion is None:
        self.quaternion = [0.] * 4
      if self.gyroscope is None:
        self.gyroscope = [0.] * 3
      if self.acceleration is None:
        self.acceleration = [0.] * 3
      if self.rpy is None:
        self.rpy = [0.] * 3
      if self.temp is None:
        self.temp = 0.
    else:
      self.quaternion = [0.] * 4
      self.gyroscope = [0.] * 3
      self.acceleration = [0.] * 3
      self.rpy = [0.] * 3
      self.temp = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      buff.write(_get_struct_4f().pack(*self.quaternion))
      buff.write(_get_struct_3f().pack(*self.gyroscope))
      buff.write(_get_struct_3f().pack(*self.acceleration))
      buff.write(_get_struct_3f().pack(*self.rpy))
      _x = self.temp
      buff.write(_get_struct_f().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 16
      self.quaternion = _get_struct_4f().unpack(str[start:end])
      start = end
      end += 12
      self.gyroscope = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.acceleration = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 12
      self.rpy = _get_struct_3f().unpack(str[start:end])
      start = end
      end += 4
      (self.temp,) = _get_struct_f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      buff.write(self.quaternion.tostring())
      buff.write(self.gyroscope.tostring())
      buff.write(self.acceleration.tostring())
      buff.write(self.rpy.tostring())
      _x = self.temp
      buff.write(_get_struct_f().pack(_x))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 16
      self.quaternion = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=4)
      start = end
      end += 12
      self.gyroscope = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.acceleration = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 12
      self.rpy = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=3)
      start = end
      end += 4
      (self.temp,) = _get_struct_f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3f = None
def _get_struct_3f():
    global _struct_3f
    if _struct_3f is None:
        _struct_3f = struct.Struct("<3f")
    return _struct_3f
_struct_4f = None
def _get_struct_4f():
    global _struct_4f
    if _struct_4f is None:
        _struct_4f = struct.Struct("<4f")
    return _struct_4f
_struct_f = None
def _get_struct_f():
    global _struct_f
    if _struct_f is None:
        _struct_f = struct.Struct("<f")
    return _struct_f
