using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class carSpawner2 : MonoBehaviour
{
    public GameObject spawnPoint;
    public GameObject car;
    public List<GameObject> path;

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
            GameObject Car = Instantiate(car, spawnPoint.transform.position, spawnPoint.transform.rotation);
            Car.GetComponent<car2>().path = path;
            time = timer;
        }
        else
        {
            time -= Time.deltaTime;
        }
    }
}
