using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class stoplichtManager : MonoBehaviour
{
    public GameObject stoplicht;
    int stoplichtStatus;

    public Material red;
    public Material green;

    float timer = 2f;
    float time = 0;

    // Start is called before the first frame update
    void Start()
    {
        stoplichtStatus = 0;
    }

    // Update is called once per frame
    void Update()
    {
        if (stoplichtStatus == 0)
        {
            stoplicht.GetComponent<Renderer>().material = red;
        }
        else if (stoplichtStatus == 1)
        {
            stoplicht.GetComponent<Renderer>().material = green;
        }

        if (time <= 0)
        {
            time = timer;
            if (stoplichtStatus == 0)
            {
                stoplichtStatus = 1;
            }
            else if (stoplichtStatus == 1)
            {
                stoplichtStatus = 0;
            }
        }
        else
        {
            time -= Time.deltaTime;
        }
    }
}
