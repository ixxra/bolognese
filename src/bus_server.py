from gi.repository import GLib
from gi.repository import Gio

introspection_xml = '''<node>
    <interface name='me.ixxra.Interface'>
      <annotation name='org.gtk.GDBus.Annotation' value='OnInterface'/>
      <annotation name='org.gtk.GDBus.Annotation' value='AlsoOnInterface'/>
      <method name='hello'>
        <annotation name='org.gtk.GDBus.Annotation' value='OnMethod'/>
        <arg type='s' name='greeting' direction='in'/>
        <arg type='s' name='response' direction='out'/>
      </method>
      <method name='EmitSignal'>
        <arg type='d' name='speed_in_mph' direction='in'>
          <annotation name='org.gtk.GDBus.Annotation' value='OnArg'/>
        </arg>
      </method>
      <method name='GimmeStdout'/>
      <signal name='VelocityChanged'>
        <annotation name='org.gtk.GDBus.Annotation' value='Onsignal'/>
        <arg type='d' name='speed_in_mph'/>
        <arg type='s' name='speed_as_string'>
          <annotation name='org.gtk.GDBus.Annotation' value='OnArg_NonFirst'/>
        </arg>
      </signal>
      <property type='s' name='FluxCapicitorName' access='read'>
        <annotation name='org.gtk.GDBus.Annotation' value='OnProperty'>
          <annotation name='org.gtk.GDBus.Annotation' value='OnAnnotation_YesThisIsCrazy'/>
        </annotation>
      </property>
      <property type='s' name='Title' access='readwrite'/>
      <property type='s' name='ReadingAlwaysThrowsError' access='read'/>
      <property type='s' name='WritingAlwaysThrowsError' access='readwrite'/>
      <property type='s' name='OnlyWritable' access='write'/>
      <property type='s' name='Foo' access='read'/>
      <property type='s' name='Bar' access='read'/>
    </interface>
  </node>'''


def handle_method_call(
    conn,
    sender,
    path,
    interface,
    method,
    args,
    invocation):
    print ('method:')
    if method == 'HelloWorld':
        print('hello')


def handle_get_property(
    conn,
    sender,
    path,
    interface,
    property,
    data):
    print ('get property')
    return 0


def handle_set_property(
    conn,
    sender,
    path,
    interface,
    property,
    value,
    data):
    pass

def ex(self):
    print('000')
    return 0

class Table(Gio.DBusInterfaceVTable):
    def method_call(self,
        conn,
        sender,
        path,
        interface,
        method,
        args,
        invocation):
        print('method call')
        if method == 'HelloWorld':
            print('hello')


    def get_property(self):
        pass

    def set_property(self):
        pass

vt = Gio.DBusInterfaceVTable()
vt.get_property = handle_get_property
vt.set_property = handle_set_property
vt.method_call = handle_method_call


#vt.method_call = f
#vtable.get_property = handle_get_property
#vtable.set_property = handle_set_property

def on_bus_acquired(conn, name):
    interfaces = Gio.DBusNodeInfo.new_for_xml(introspection_xml).interfaces[0]

    conn.register_object('/me/ixxra/Player',
                         interfaces,
                         vt,
                         None,
                         lambda *args: 0)


def on_name_acquired(conn, name):
    print('name acquired:', conn, name)


def on_name_lost(conn, name):
    print('name lost:', conn, name)


id = Gio.bus_own_name(Gio.BusType.SESSION,
        'me.ixxra.server',
        Gio.BusNameOwnerFlags.ALLOW_REPLACEMENT,
        on_bus_acquired,
        on_name_acquired,
        on_name_lost)

loop = GLib.MainLoop()
loop.run()

Gio.bus_unown_name(id)
