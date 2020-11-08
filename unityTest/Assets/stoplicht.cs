using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.IO;
using System;
using Newtonsoft.Json;
using Newtonsoft.Json.Linq;

public class stoplicht : MonoBehaviour
{
    public GameObject Stoplicht;
    Renderer sl;
    public Material green;
    public Material red;

    public int status = 0;
    public int hasCar = 0;
    public int hasCarTimer;
    public int hasCarMax = 5;

    float timer = 5f;
    float time = 0;

    // Start is called before the first frame update
    void Start()
    {
        sl = Stoplicht.GetComponent<Renderer>();
    }

    //Update is called once per frame
    void Update()
    {
        if (status == 0)
        {
            sl.material = red;
        }
        else if (status == 1)
        {
            sl.material = green;
        }

        jason jsn = jason.instance;

        //if (hasCarTimer <= 0)
        //{
        //    hasCar = 0;

        //    jsn.jobj["A1-1"] = "0";
        //}
        //else
        //{
        //    hasCarTimer--;

        //    //jsn.jobj["A1-1"] = "1";
        //}

        StartCoroutine("changeJson", jsn);
    }

    IEnumerator changeJson(jason jsn)
    {
        if (hasCar == 1)
        {
            jsn.jobj[transform.name] = "1";
        }
        else if (hasCar == 0)
        {
            jsn.jobj[transform.name] = "0";
        }

        yield return new WaitForSeconds(0.2f);
    }
}
