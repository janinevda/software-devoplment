using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class carSpawnManager : MonoBehaviour
{
    public List<GameObject> spawnPoints = new List<GameObject>();

    public float spawnDelay = 2f;

    // Start is called before the first frame update
    void Start()
    {
        StartCoroutine("spawn");
    }

    IEnumerator spawn()
    {
        while (true)
        {
            yield return new WaitForSeconds(spawnDelay);

            int rnd = UnityEngine.Random.Range(0, spawnPoints.Count);
            spawnPoints[rnd].GetComponent<carSpawner3>().StartCoroutine("spawnCar");
        }
    }

    // Update is called once per frame
    void Update()
    {
        
    }
}
