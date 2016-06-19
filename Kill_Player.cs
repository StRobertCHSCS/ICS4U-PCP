using UnityEngine;
using System.Collections;

public class Kill_Player : MonoBehaviour {

    public Level_manager level_manager;

    // Use this for initialization
	void Start () {
        level_manager = FindObjectOfType<Level_manager>();
	}
	
	// Update is called once per frame
	void Update () {
	
	}

    void OnTriggerEnter2D(Collider2D collide)
    {
        if(collide.name == "Scorpion")
        {
            level_manager.Respawn_Player();
        }
    }
}
