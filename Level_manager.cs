using UnityEngine;
using System.Collections;

public class Level_manager : MonoBehaviour {

    public GameObject current_respawnpoint;

    // call player script and set it to variable
    private NewBehaviourScript scorpion;

	// Use this for initialization
	void Start () {
        scorpion = FindObjectOfType<NewBehaviourScript>();
	
	}
	
	// Update is called once per frame
	void Update () {
	
	}

    // check to see if collider hits player and then have player respawn at specific spot
    public void Respawn_Player()
    {
        Debug.Log("Player Respawn");
        scorpion.transform.position = current_respawnpoint.transform.position;
    }
}
