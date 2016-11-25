### Asset Store window is blank
Try to undock Asset Store window -_-!  

### draw 2D texture to screen

  ```csharp
  public class camera : MonoBehaviour {
    private Texture tex;
    void Start () {
      tex = Resources.Load ("expl_big") as Texture;
    }

    void OnGUI() {
      if (!Event.current.type.Equals (EventType.Repaint))
        return;
      // In normalized coordinates with (0,0) in the bottom-left corner.
      Rect rc_tex = new Rect (0.25F, 0.5F, 0.248F, 0.2477F);
      //  In pixel coordinates with (0,0) in the upper-left corner.
      Rect rc_dest = new Rect (0, 0, 256, 219);
      if (tex != null) {
        //Graphics.DrawTexture(rc_dest,tex);
        Graphics.DrawTexture (rc_dest, tex, rc_tex, 0, 0, 0, 0); 
      }
    }
  }
  ```
