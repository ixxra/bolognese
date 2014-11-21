
[DBus (name="me.ixxra.Player")]
public class Player: Object {
    private dynamic Gst.Element playbin;
    private Gee.LinkedList<string> playlist;
    private Gee.BidirListIterator<string> iter;

    public Player(){
        playlist = new Gee.LinkedList<string> ();
        iter = playlist.bidir_list_iterator();
    }

    private void _on_message(Gst.Bus bus, Gst.Message msg){
        switch (msg.type){
            case Gst.MessageType.EOS:
                stdout.printf("THE END\n");
                break;
        }
    }

    private void _play(string fname){
        playbin = Gst.ElementFactory.make("playbin", "playbin");
        playbin.bus.add_signal_watch();
        playbin.bus.message.connect(_on_message);

        try{
            var uri = Gst.filename_to_uri(fname);    
            playbin.uri = uri;
            playbin.set_state(Gst.State.PLAYING);
        } catch (GLib.Error err) {

        }
    }

    public void play(){
        if (!iter.next()){
            return;
        }
        var fname = iter.get();
        _play(fname);
    }

    public void stop() {
        if (playbin == null) {
            return;
        }

        playbin.set_state(Gst.State.NULL);
    }

    public void pause(){
        if (playbin == null){
            return;
        }

        playbin.set_state(Gst.State.PAUSED);
    }

    public bool nex(){
        return iter.next();
    }

    public bool prev(){
        return iter.previous();
    }

    public void jump(int pos){
        return;
    }

    public void add(string fname){
        playlist.add(fname);
    }
}

void on_bus_aquired(DBusConnection conn) {
    try {
        conn.register_object("/me/ixxra/Player", new Player());
    } catch (IOError err) {
        stderr.printf("Could not register service\n");
    }
}

void main(string[] args){
    Gst.init(ref args);
    Bus.own_name(BusType.SESSION, "me.ixxra.Server", BusNameOwnerFlags.NONE, 
        on_bus_aquired,
        () => {},
        () => stderr.printf("Could not aquire name\n"));

    new MainLoop().run();
}