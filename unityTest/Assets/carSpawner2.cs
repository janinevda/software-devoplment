using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class carSpawner2 : MonoBehaviour
{
    public GameObject sP;
    public GameObject car;

    public float timer = 10f;
    public float time = 0f;

    // Start is called before the first frame update
    void Start()
    {
        
    }

    // Update is called once per frame
    void Update()
    {
        if (time <= 0)
        {
            GameObject Car = Instantiate(car, sP.transform.position, sP.transform.rotation);
            spawnPoint spawnpoint = sP.GetComponent<spawnPoint>();
            if (spawnpoint.numPaths == 1)
            {
                Car.GetComponent<car2>().path = spawnpoint.path1;
            }
            else if (spawnpoint.numPaths == 2)
            {
                int rnd = UnityEngine.Random.Range(0, 2);
                if (rnd == 0)
                {
                    Car.GetComponent<car2>().path = spawnpoint.path1;
                }
                else
                {
                    Car.GetComponent<car2>().path = spawnpoint.path2;
                }

            }
            
            time = timer;
        }
        else
        {
            time -= Time.deltaTime;
        }
    }
}
