using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using Newtonsoft.Json.Linq;

public class jason : MonoBehaviour
{
    public static jason instance = new jason();

    string path = "assets/jason_simulation (1).json";
    string json;
    public JObject jobj;
    public JObject channel;

    private void Start()
    {
        instance.json = System.IO.File.ReadAllText(path);
        instance.jobj = JObject.Parse(instance.json);
        instance.channel = (JObject)instance.jobj;
    }
}
