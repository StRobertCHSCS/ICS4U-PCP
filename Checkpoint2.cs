using UnityEngine;
using System.Collections;

public class Checkpoint2 : MonoBehaviour
{

    public LevelManager2 levelManager2;

    // Use this for initialization
    void Start()
    {
        levelManager2 = FindObjectOfType<LevelManager2>();
    }

    // Update is called once per frame
    void Update()
    {

    }

    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.name == "MarioController")
        {
            levelManager2.currentCheckpoint2 = gameObject;
        }
    }
}